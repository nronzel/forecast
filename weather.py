import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1"

if API_KEY is None:
    raise ValueError("API key not found or provided")


def fetch_weather():
    api = f"key={API_KEY}"
    location = "&q=auto:ip"

    url = BASE_URL + "/current.json?" + api + location
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed with status code: {response.status_code}")


def parse_weather(data):
    current_weather = data["current"]

    weather = {
        "temp": current_weather["temp_f"],
        "feels_like": current_weather["feelslike_f"],
        "humidity": current_weather["humidity"],
        "uv_index": current_weather["uv"],
        "precip": current_weather["precip_in"],
        "wind": current_weather["wind_mph"],
        "gusts": current_weather["gust_mph"],
    }


    return weather


def parse_location(data):
    location = data["location"]

    return location
