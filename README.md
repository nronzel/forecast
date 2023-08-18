# Fore!Cast

## Description

Fetches the weather based on IP address, and let's you know whether you can
go golfing or not.

![screenshot](./output.png)

### API Requirements

Requires a [WeatherAPI](https://www.weatherapi.com/) free tier key to use.

It will ask for your API key if it doesn't detect one in a .env file. The
provided key will be written to the `WEATHER_API_KEY` variable in a .env file
at the root of the project.
