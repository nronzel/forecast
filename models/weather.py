from conditions.evaluator import *


class Weather:
    """
    A class to represent and evaluate weather conditions.

    Attributes:
        weather (dict): A dictionary containing cleaned weather data.
        evaluator_instances (dict): A dictionary containing evaluator instances
        for each weather condition.

    Methods:
        evaluate_conditions() -> int:
            Calculates and returns the average score of all weather conditions.

        find_worst_conditions() -> List[str]:
            Identifies and returns a list of the worst weather conditions based
            on their scores.

        _clean_data(weather_data: dict) -> dict:
            Cleans and transforms the raw weather data into a usable format.
    """

    def __init__(self, weather_data, evaluators=None):
        """
        Constructs the Weather object with provided weather data and evaluators.

        Args:
            weather_data (dict): The raw weather data to be processed.
            evaluators (dict, optional): A dictionary containing evaluator
            classes for each weather condition (mainly used for testing new
            evaluators). Defaults to built-in evaluators.
        """
        self.weather = self._get_clean_data(weather_data)

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
        """
        Evaluates the overall weather conditions based on individual condition
        scores.

        Returns:
            int: The average score of all evaluated weather conditions.
        """
        total_score = sum(
            evaluator.evaluate() for evaluator in self.evaluator_instances.values()
        )
        average_score = total_score / len(self.evaluator_instances)
        return round(average_score)

    def _find_worst_conditions(self):
        """
        Identifies the weather conditions with the lowest scores.

        Returns:
            List[str]: A list of weather conditions with the worst scores.
        """
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

    def _get_clean_data(self, weather_data):
        """
        Cleans and structures raw weather data for relevent info for further
        processing

        Args:
            weather_data (dict): The raw weather data to be cleaned.

        Returns:
            dict: The cleaned weather data.
        """
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
        """
        Displays the weather data and worst conditions in a formatted manner
        with borders.

        The method first prints out the cleaned weather data, followed by the
        worst conditions identified by the find_worst_conditions method.

        Example Output:
        +----------------------------------------+
        |               Weather Data             |
        +----------------------------------------+
        | Temperature    :                  75.0 |
        | Humidity       :                    60 |
        +----------------------------------------+
        |             What Sucks Today           |
        +----------------------------------------+
        |                Humidity                |
        +----------------------------------------+
        """

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
        worst_conditions = self._find_worst_conditions()
        print("|{:^40}|".format(" What Sucks Today "))
        print_line()
        for condition in worst_conditions:
            print("|{:^40}|".format(condition.capitalize()))
        print_line()
