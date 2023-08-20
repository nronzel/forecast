class Parser:
    def __init__(self, raw_data, hour=None):
        self.raw_data = raw_data
        self.location_parser = LocationParser(self.raw_data)
        self.parsed_location_data = self.location_parser.parse()

        self.hour = hour
        if hour is None:
            self.hour = self._get_current_hour()

        self.weather_parser = WeatherParser(self.raw_data, self.hour)
        self.parsed_weather_data = self.weather_parser.parse()

    def _get_current_hour(self):
        try:
            time = self.parsed_location_data["localtime"]
            return int(time.split(" ")[1].split(":")[0])
        except KeyError as e:
            print(f"Missing key in raw location data: {e}")


class LocationParser:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def parse(self):
        try:
            location_data = self.raw_data["location"]
            return {
                "city": location_data["name"],
                "state": location_data["region"],
                "localtime": location_data["localtime"],
            }
        except KeyError as e:
            print(f"Missing key in raw location data: {e}")
            return {}


class WeatherParser:
    def __init__(self, raw_data, hour=None):
        self.raw_data = raw_data
        self.hour = hour

    def parse(self):
        current_weather_parser = CurrentWeatherParser(self.raw_data)
        todays_forecast_parser = TodaysForecastParser(self.raw_data)
        hourly_weather_parser = HourlyWeatherParser(self.raw_data, self.hour)

        return {
            "current_weather": current_weather_parser.parse(),
            "todays_forecast": todays_forecast_parser.parse(),
            "hourly_weather": hourly_weather_parser.parse(),
        }


class CurrentWeatherParser:
    def __init__(self, raw_data):
        self.raw_data = raw_data["current"]

    def parse(self):
        try:
            return {
                "temp": self.raw_data["temp_f"],
                "feels_like": self.raw_data["feelslike_f"],
                "humidity": self.raw_data["humidity"],
                "uv": self.raw_data["uv"],
                "wind": self.raw_data["wind_mph"],
                "gust": self.raw_data["gust_mph"],
                "condition": self.raw_data["condition"]["text"],
            }

        except KeyError as e:
            print(f"Missing key in raw current weather data: {e}")
            return {}


class HourlyWeatherParser:
    def __init__(self, raw_data, hour):
        self.raw_data = raw_data["forecast"]["forecastday"][0]["hour"]
        self.hour = hour

    def parse(self):
        if self.hour is not None:
            self.hour = int(self.hour)

        data = self.raw_data[self.hour]
        return {
            "temp": data["temp_f"],
            "feels_like": data["feelslike_f"],
            "humidity": data["humidity"],
            "uv": data["uv"],
            "wind": data["wind_mph"],
            "gust": data["gust_mph"],
            "rain_chance": data["chance_of_rain"],
            "snow_chance": data["chance_of_snow"],
        }


class TodaysForecastParser:
    def __init__(self, raw_data):
        self.raw_data = raw_data["forecast"]["forecastday"][0]["day"]

    def parse(self):
        return {
            "avg_temp": self.raw_data["avgtemp_f"],
            "max_wind": self.raw_data["maxwind_mph"],
            "avg_humidity": self.raw_data["avghumidity"],
            "rain_chance": self.raw_data["daily_chance_of_rain"],
            "snow_chance": self.raw_data["daily_chance_of_snow"],
            "condition": self.raw_data["condition"]["text"],
        }
