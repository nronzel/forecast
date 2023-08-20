from conditions.evaluator import *
from conditions.global_evaluators import (
    TodaysForecastEvaluator,
    CurrentWeatherEvaluator,
    HourlyWeatherEvaluator,
)
from api.parser import Parser


class Weather:
    """
    A class to represent and evaluate weather conditions.
    """

    def __init__(self, weather_data):
        """
        Constructs the Weather object with provided weather data and evaluators.
        """
        self.parser = Parser(weather_data)
        self.todays_forecast_evaluator = TodaysForecastEvaluator(
            self.parser.parsed_weather_data["todays_forecast"]
        )
        self.current_weather_evaluator = CurrentWeatherEvaluator(
            self.parser.parsed_weather_data["current_weather"]
        )
        self.hourly_weather_evaluator = HourlyWeatherEvaluator(
            self.parser.parsed_weather_data["hourly_weather"]
        )
        self.location_data = self.parser.parsed_location_data

    def evaluate_conditions(self):
        """
        Evaluates the overall weather conditions based on individual condition
        scores.
        """
        todays_forecast_score = self.todays_forecast_evaluator.evaluate()
        current_weather_score = self.current_weather_evaluator.evaluate()
        total = todays_forecast_score + current_weather_score
        average_score = total / 2
        return round(average_score)

    def get_location_data(self):
        return self.parser.parsed_location_data

    def _find_worst_conditions(self):
        """
        Identifies the weather conditions with the lowest scores.
        """
        scores = {
            "Today's Forecast": self.todays_forecast_evaluator.evaluate(),
            "Current Weather": self.current_weather_evaluator.evaluate(),
            "Hourly Weather": self.hourly_weather_evaluator.evaluate(),
        }

        min_score = min(scores.values())
        worst = [condition for condition, score in scores.items() if score == min_score]
        return worst

    def pretty_print(self):
        """
        Displays the weather, location data, and worst conditions in a formatted
        manner with borders.
        """

        def print_line():
            print("+" + "-" * 40 + "+")

        # Print the location data with a border
        print_line()
        print("|{:^40}|".format(" Location Data "))
        print_line()
        for key, value in self.location_data.items():
            print("| {:<15} : {:>20} |".format(key.capitalize(), value))
        print_line()

        # Print the weather data with a border
        print_line()
        print("|{:^40}|".format(" Weather Data "))
        print_line()
        print(
            "| Today's Forecast Score : {:>11} |".format(
                self.todays_forecast_evaluator.evaluate()
            )
        )
        print(
            "| Current Weather Score  : {:>11} |".format(
                self.current_weather_evaluator.evaluate()
            )
        )
        print(
            "| Hourly Weather Score   : {:>11} |".format(
                self.hourly_weather_evaluator.evaluate()
            )
        )
        print_line()

        # Find and print the worst conditions with a border
        worst_conditions = self._find_worst_conditions()
        print("|{:^40}|".format(" What Sucks Today "))
        print_line()
        for condition in worst_conditions:
            print("|{:^40}|".format(condition))
        print_line()
