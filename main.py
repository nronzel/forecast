from api.weather_fetcher import WeatherFetcher
from models.checker import WeatherChecker

if __name__ == "__main__":
    location = input("Enter your location (or leave empty for auto): ")
    if location == "":
        location = "auto:ip"

    fetcher = WeatherFetcher(location)
    weather_data = fetcher.fetch_weather()

    checker = WeatherChecker(weather_data)

    print(checker.can_golf())
