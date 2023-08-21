# Fore!Cast

## Description

Fetches the weather and let's you know whether you can go golfing or not.

Uses a provided location, or if no location is provided it defaults to IP
address geolocation. This default is not very accurate, and may get a city near
you but not your exact location.

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

### The Scores

Each weather condition is evaluated on a scale of **1 - 10**. With 10 being ideal
conditions, and 1 being horrible conditions (hot, very humid or dry, windy, etc.)

TODO:

- [ ] Input Sanitization for location & api key
