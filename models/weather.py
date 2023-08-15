from conditions.evaluator import *


class Weather:
    def __init__(self, weather_data):
        self.temp_evaluator = TempEvaluator(weather_data["temp"])
        # ...other evaluators (humidity, precip, etc.)

    def evaluate_conditions(self):
        temp_score = self.temp_evaluator.evaluate()

        # combined_score here

        return temp_score
