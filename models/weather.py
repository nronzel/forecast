from conditions.evaluator import *


class Weather:
    def __init__(self, weather_data, evaluators=None):
        self.weather = self._clean_data(weather_data)

        if evaluators is None:
            evaluators = {
                "temp": TempEvaluator,
                "feels_like": FeelsLikeEvaluator,
                "humidity": HumidityEvaluator,
                "uv": UvEvaluator,
                "wind": WindEvaluator,
                "gust": GustEvaluator,
            }

        self.evaluator_instances = {}
        for key, Evaluator in evaluators.items():
            if key in self.weather:
                self.evaluator_instances[key] = Evaluator(self.weather[key])

    def evaluate_conditions(self):
        total_score = sum(
            evaluator.evaluate() for evaluator in self.evaluator_instances.values()
        )
        average_score = total_score / len(self.evaluator_instances)
        return round(average_score)

    def find_worst_conditions(self):
        scores = {}
        for condition, eval_instance in self.evaluator_instances.items():
            score = eval_instance.evaluate()
            scores[condition] = score

        min_score = min(scores.values())

        worst = []
        for condition, score in scores.items():
            if score == min_score:
                worst.append(condition)

        return worst

    def _clean_data(self, weather_data):
        c = weather_data["current"]
        clean_weather = {
            "temp": c["temp_f"],
            "feels_like": c["feelslike_f"],
            "humidity": c["humidity"],
            "uv": c["uv"],
            "wind": c["wind_mph"],
            "gust": c["gust_mph"],
            # "precip": c["precip_in"],
        }

        return clean_weather

    def pretty_print(self):
        # Helper function to print a horizontal line
        def print_line():
            print("+" + "-" * 40 + "+")

        # Print the weather data with a border
        print_line()
        print("|{:^40}|".format(" Weather Data "))
        print_line()
        for key, value in self.weather.items():
            print("| {:<15} : {:>20} |".format(key.capitalize(), value))
        print_line()

        # Find and print the worst conditions with a border
        worst_conditions = self.find_worst_conditions()
        print("|{:^40}|".format(" Worst Conditions "))
        print_line()
        for condition in worst_conditions:
            print("|{:^40}|".format(condition.capitalize()))
        print_line()
