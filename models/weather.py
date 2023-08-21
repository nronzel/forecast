from conditions.global_evaluators import (
    TodaysForecastEvaluator,
    CurrentWeatherEvaluator,
    HourlyWeatherEvaluator,
)
from conditions.condition_evaluators import ConditionEvaluator
from api.parser import Parser
from .pretty_printer import PrettyPrinter


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

    def evaluate_conditions(self):
        """
        Evaluates the overall weather conditions based on individual condition
        scores.
        """
        todays_forecast_score = self.todays_forecast_evaluator.evaluate()
        current_weather_score = self.current_weather_evaluator.evaluate()
        hourly_weather_score = self.hourly_weather_evaluator.evaluate()
        total = todays_forecast_score + current_weather_score + hourly_weather_score
        average_score = total / 3
        return round(average_score)

    def get_location_data(self):
        return self.parser.parsed_location_data

    def get_todays_condition(self):
        return self.parser.parsed_weather_data["todays_forecast"]["condition"]

    def evaluate_worst_conditions(self):
        condition_evaluator = ConditionEvaluator(
            self.todays_forecast_evaluator,
            self.current_weather_evaluator,
            self.hourly_weather_evaluator,
        )
        worst_conditions = condition_evaluator.evaluate()
        filtered_worst_conditions = condition_evaluator.filter_worst_conditions(
            worst_conditions
        )
        return filtered_worst_conditions

    def pretty_print(self):
        worst_conditions = self.evaluate_worst_conditions()
        printer = PrettyPrinter(self, worst_conditions)
        printer.print()
