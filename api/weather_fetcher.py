import os
import requests
from dotenv import load_dotenv, set_key
from urllib.parse import urlencode


class WeatherFetcher:
    _BASE_URL = "https://api.weatherapi.com/v1"
    _DEFAULT_DAYS = 1
    _DEFAULT_AQI = "no"  # Air Quality Index
    _DEFAULT_ALERTS = "no"  # Weather Alerts
    _ENV_FILE = ".env"
    _API_KEY_ENV_VAR = "WEATHER_API_KEY"

    def __init__(self, location):
        self._api_key = self._load_api_key()
        self._location = location

    @classmethod
    def _write_api_key_to_env(cls, api_key):
        set_key(cls._ENV_FILE, cls._API_KEY_ENV_VAR, api_key)

    @classmethod
    def _load_api_key(cls):
        load_dotenv(cls._ENV_FILE)
        api_key = os.environ.get(cls._API_KEY_ENV_VAR)
        if not api_key:
            key = input("Please enter your API key: ")
            cls._write_api_key_to_env(key)
            return key
        return api_key

    def _get_params(self, days, aqi, alerts):
        return {
            "key": self._api_key,
            "q": self._location,
            "days": days,
            "aqi": aqi,
            "alerts": alerts,
        }

    def _build_url(self, days: int, aqi="no", alerts="no"):
        endpoint = "/forecast.json"
        query_string = urlencode(self._get_params(days, aqi, alerts))
        return f"{self._BASE_URL}{endpoint}?{query_string}"

    def fetch_weather(self, days: int = 1, aqi="no", alerts="no"):
        url = self._build_url(days, aqi, alerts)
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
