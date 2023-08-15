from conditions.evaluator import *


class Weather:
    def __init__(self, weather_data):
        self.weather = self.__clean_data(weather_data)
        self.temp_evaluator = TempEvaluator(self.weather["temp"])
        # ...other evaluators (humidity, precip, etc.)

    def evaluate_conditions(self):
        temp_score = self.temp_evaluator.evaluate()

        # combined_score here

        # TODO: return combined score
        return temp_score

    def __clean_data(self, weather_data):
        c = weather_data["current"]
        clean_weather = {"temp": c["temp_f"]}

        return clean_weather
