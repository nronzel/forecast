from conditions import evaluator
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
        return average_score

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
