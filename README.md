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

## How It Works

Upon fetching the weather, it determines an overall score for the day based on
the weather data retrieved. The score is then used to determine what response
is chosen and shown to the user.

In a future release I will be adding more responses based on the worst
weather conditions of the day.
