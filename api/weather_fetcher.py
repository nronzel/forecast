import os
import requests
from dotenv import load_dotenv, set_key
from urllib.parse import urlencode
from models.input_verifier import ApiKeyVerifier, LocationVerifier


class WeatherFetcher:
    _BASE_URL = "https://api.weatherapi.com/v1"
    _DEFAULT_DAYS = 1
    _DEFAULT_AQI = "no"  # Air Quality Index
    _DEFAULT_ALERTS = "no"  # Weather Alerts
    _ENV_FILE = ".env"
    _API_KEY_ENV_VAR = "WEATHER_API_KEY"

    def __init__(self, location=None):
        self._api_key = self._load_api_key()
        self._location = location

    @classmethod
    def _write_api_key_to_env(cls, api_key):
        valid = cls._check_api_key(api_key)
        if not valid:
            print("Invalid API key provided. Please check and try again.")
        set_key(cls._ENV_FILE, cls._API_KEY_ENV_VAR, api_key)

    @classmethod
    def _load_api_key(cls):
        load_dotenv(cls._ENV_FILE)
        api_key = os.environ.get(cls._API_KEY_ENV_VAR)
        if not api_key:
            key = input(
                """
                Please provide a free tier WeatherAPI API key.
                Any key provided here is just written to a .env file
                at the root of the project.
                """
            )
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

    def get_location(self):
        while True:
            location = input("Enter your location (or leave empty for auto): ")
            if location == "":
                location = "auto:ip"
                self._location = location
                break
            valid = self._check_location(location)
            self._location = location
            if not valid or not self._test_location():
                print("Invalid location, please check and try again.")
                self._location = None
            else:
                self._location = location
                break

    def _build_url(self, days: int, aqi="no", alerts="no"):
        endpoint = "/forecast.json"
        query_string = urlencode(self._get_params(days, aqi, alerts))
        return f"{self._BASE_URL}{endpoint}?{query_string}"

    def fetch_weather(self, days: int = 1, aqi="no", alerts="no"):
        url = self._build_url(days, aqi, alerts)
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def _test_location(self):
        url = self._build_url(1, "no", "no")
        response = requests.get(url)
        if response.status_code != 200:
            return False
        return True

    def _check_location(self, location):
        location_verifier = LocationVerifier(location)
        return location_verifier.verify()

    def _check_api_key(self):
        api_key_verifier = ApiKeyVerifier(self._api_key)
        return api_key_verifier.verify()
