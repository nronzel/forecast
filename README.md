# Fore!Cast

## Description

Fetches the weather based on IP address, and let's you know whether you can
go golfing or not.

![screenshot](./output.png)

### API Requirements

Requires a [WeatherAPI](https://www.weatherapi.com/) free tier key to use.

Create a file in the project directory called `.env` and add your API key.
The variable must be called `WEATHER_API_KEY` in order for the key to be properly
read. See example below.

```
# example .env file
WEATHER_API_KEY=YourApiKeyHere
```

## TODO

- [ ] Change data source from current to forecast to get precip_chance
    - [ ] evaluator for precipitation precip_chance
    - [ ] add precip_chance to test
- [ ] Add location data to output

