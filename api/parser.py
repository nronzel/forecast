class Parser:
    def __init__(self, raw_data):
        self.parsed_weather_data = self._parse_weather_data(raw_data)
        self.parsed_location_data = self._parse_location_data(raw_data)

    def _parse_weather_data(self, raw_data):
        return {
            "todays_forecast": self._parse_todays_forecast(
                raw_data["forecast"]["forecastday"][0]["day"]
            ),
            "current_weather": self._parse_current_weather(raw_data["current"]),
            "hourly_weather": self._parse_hourly_weather(
                raw_data["forecast"]["forecastday"][0]["hour"]
            ),
        }

    def _parse_location_data(self, raw_data):
        location_data = raw_data["location"]
        parsed_data = {
            "city": location_data["name"],
            "state": location_data["region"],
            "localtime": location_data["localtime"],
        }
        return parsed_data

    def _parse_current_weather(self, current_weather_data):
        return {
            "temp": current_weather_data["temp_f"],
            "wind": current_weather_data["wind_mph"],
            "gust": current_weather_data["gust_mph"],
            "humidity": current_weather_data["humidity"],
            "feels_like": current_weather_data["feelslike_f"],
            "uv": current_weather_data["uv"],
            "current_condition": current_weather_data["condition"]["text"],
        }

    def _parse_todays_forecast(self, todays_forecast_data):
        return {
            "avg_temp": todays_forecast_data["avgtemp_f"],
            "max_wind": todays_forecast_data["maxwind_mph"],
            "avg_humidity": todays_forecast_data["avghumidity"],
            "rain_chance": todays_forecast_data["daily_chance_of_rain"],
            "snow_chance": todays_forecast_data["daily_chance_of_snow"],
            "todays_condition": todays_forecast_data["condition"]["text"],
        }

    def _parse_hourly_weather(self, hourly_weather_data):
        print(hourly_weather_data)
