from api.weather_fetcher import WeatherFetcher
from models.checker import WeatherChecker

if __name__ == "__main__":
    fetcher = WeatherFetcher()
    fetcher.get_location()
    weather_data = fetcher.fetch_weather()

    checker = WeatherChecker(weather_data)

    print(checker.can_golf())
