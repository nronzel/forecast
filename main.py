from api.weather import *


def main():
    data = fetch_today_weather()
    weather = parse_today_weather(data)
    location = parse_location(data)
    print(weather)
    print(location)


if __name__ == "__main__":
    main()
