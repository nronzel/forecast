import os
import requests
from dotenv import load_dotenv


class WeatherFetcher:
    def __init__(self, location="auto:ip"):
        load_dotenv()
        self.__api_key = os.environ.get("WEATHER_API_KEY")

        if self.__api_key is None:
            raise ValueError("API key not found or provided")

        self.location = location # defaults to IP address lookup
        self.forecast = False  # defaults to current weather
        self.__base_url = "https://api.weatherapi.com/v1"


    def fetch_weather(self):
        period = "/forecast.json?" if self.forecast else "/current.json?"
        key = f"key={self.__api_key}"
        url = self.__base_url + period + key

        response = requests.get(url)
        response.raise_for_status()

        return response.json()
