from .weather import Weather
from responses.response_manager import ResponseManager


class WeatherChecker:
    def __init__(self, weather_data):
        self.weather = Weather(weather_data)
        self.response_manager = ResponseManager()

    def can_golf(self):
        combined_score = self.weather.evaluate_conditions()

        self.weather.pretty_print()
        return self.response_manager.get_response(combined_score)
