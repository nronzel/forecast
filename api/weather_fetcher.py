import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("WEATHER_API_KEY")

if API_KEY is None:
    raise ValueError("API key not found or provided")


class WeatherFetcher:
    _base_url = "https://api.weatherapi.com/v1"

    def __init__(self, location):
        self._api_key = API_KEY
        self._location = location

        # Defaults to current weather. This exists for future expansion.
        self._forecast = False

    def fetch_weather(self):
        period = "/forecast.json?" if self._forecast else "/current.json?"
        key = f"key={self._api_key}"
        location = f"&q={self._location}"
        url = self._base_url + period + key + location

        response = requests.get(url)
        response.raise_for_status()

        return response.json()
