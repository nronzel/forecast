import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1"

if API_KEY is None:
    raise ValueError("API key not found or provided")


def fetch_today_weather(location="auto:ip"):
    """
    Fetches the current weather based on the IP address by default,
    or by the provided location.

    Locations can be:
        City, State
        Zip code
        Airport Code
    """
    api = f"key={API_KEY}"
    location = f"&q={location}"

    url = BASE_URL + "/current.json?" + api + location
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed with status code: {response.status_code}")
