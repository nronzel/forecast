from .weather import Weather
from responses.response_manager import ResponseManager


class WeatherChecker:
    def __init__(self, weather_data):
        self.weather = Weather(weather_data)
        self.response_manager = ResponseManager()

    def can_golf(self):
        combined_score = self.weather.evaluate_conditions()
        return self.response_manager.get_response(combined_score)


# def parse_today_weather(data):
#     current_weather = data["current"]
#
#     weather = {
#         "temp": current_weather["temp_f"],
#         "feels_like": current_weather["feelslike_f"],
#         "humidity": current_weather["humidity"],
#         "uv_index": current_weather["uv"],
#         "precip": current_weather["precip_in"],
#         "wind": current_weather["wind_mph"],
#         "gusts": current_weather["gust_mph"],
#     }
#
#     return weather
#
#
# def parse_location(data):
#     location = data["location"]
#
#     return location
