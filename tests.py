import unittest
import random

from responses.response_manager import ResponseManager
from conditions.evaluator import Evaluator
from conditions.condition_evaluators import (
    FeelsLikeEvaluator,
    GustEvaluator,
    HumidityEvaluator,
    TempEvaluator,
    UvEvaluator,
    WindEvaluator,
    RainEvaluator,
    SnowEvaluator,
)

EVALUATORS = [
    {"class": TempEvaluator, "param": "temp"},
    {"class": FeelsLikeEvaluator, "param": "feels_like"},
    {"class": HumidityEvaluator, "param": "humidity"},
    {"class": UvEvaluator, "param": "uv"},
    {"class": WindEvaluator, "param": "wind"},
    {"class": GustEvaluator, "param": "gust"},
    {"class": RainEvaluator, "param": "rain_chance"},
    {"class": SnowEvaluator, "param": "snow_chance"},
]


class TestEvaluators(unittest.TestCase):
    def evaluator_test(self, evaluator_class):
        values = generate_floats(150, 10000)

        for value in values:
            # create evaluator instance with random value
            eval = evaluator_class(value)
            score = eval.evaluate()

            # check if score is in correct range
            expected = 1
            for (min, max), s in eval.scoring_ranges:
                if min <= value <= max:
                    expected = s
                    break

            self.assertEqual(
                score, expected, f"curr {value}, expected {expected}, got {score}"
            )


class Tests(unittest.TestCase):
    def test_response_manager_responses(self):
        rm = ResponseManager()
        test_scores = generate_floats(10, 10000)

        for score in test_scores:
            response = rm.get_response(score)

            # ensure the response is not that it coudn't determine the condition
            self.assertNotEqual(
                response,
                "couldn't determine weather condition",
                f"Failed for score {score}",
            )
            # ensure score fits within expected range
            for (low, high), expected_response in ResponseManager.RESPONSES.items():
                if low <= score <= high:
                    self.assertEqual(
                        response,
                        expected_response,
                        f"curr score {score}, expected {expected_response} but got {response}",
                    )
                    break

    def test_find_score(self):
        list = [
            ((45, 50.99), 2),
            ((51, 60.99), 5),
            ((61, 65.99), 6),
            ((66, 70.99), 8),
            ((71, 79.99), 10),
            ((80, 83.99), 9),
            ((84, 86.99), 6),
            ((87, 93.99), 3),
        ]

        eval = Evaluator()
        values = generate_floats(150, 10000)
        for value in values:
            score = eval.find_score(list, value)
            expected = 1
            for (min, max), s in list:
                if min <= value <= max:
                    expected = s
                    break
                expected = 1
            self.assertEqual(
                score, expected, f"curr {value}, expected {expected}, got {score}"
            )


# loops through the EVALUATORS and tests each one
for evaluator_info in EVALUATORS:
    test_func = lambda self, e=evaluator_info: self.evaluator_test(e["class"])
    setattr(TestEvaluators, f"test_{evaluator_info['class'].__name__}", test_func)


# helpers
def generate_floats(max_num, num_amount):
    return [round(random.uniform(0, max_num), 2) for _ in range(num_amount)]


if __name__ == "__main__":
    unittest.main()
