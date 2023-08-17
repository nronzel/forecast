import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlencode, urljoin

load_dotenv()
API_KEY = os.environ.get("WEATHER_API_KEY")

if API_KEY is None:
    raise ValueError("API key not found or provided")


class WeatherFetcher:
    _base_url = "https://api.weatherapi.com/v1"

    def __init__(self, location):
        self._api_key = API_KEY
        self._location = location

    def _build_url(self, days: int, aqi="no", alerts="no"):
        endpoint = "/forecast.json"
        params = {
            "key": self._api_key,
            "q": self._location,
            "days": days,
            "aqi": aqi,
            "alerts": alerts,
        }
        query_string = urlencode(params)
        return f"{self._base_url}{endpoint}?{query_string}"

    def fetch_weather(self, days: int = 1, aqi="no", alerts="no"):
        url = self._build_url(days, aqi, alerts)
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
