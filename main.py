from weather import *

def main():
    data = fetch_weather()
    weather = parse_weather(data)
    location = parse_location(data)
    print(weather)
    print(location)


if __name__ == "__main__":
    main()
