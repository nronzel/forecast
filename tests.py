import unittest
import random
from models.input_verifier import LocationVerifier, ApiKeyVerifier

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


"""
Evaluator Testing
"""


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


# loops through the EVALUATORS and tests each one
for evaluator_info in EVALUATORS:
    test_func = lambda self, e=evaluator_info: self.evaluator_test(e["class"])
    setattr(TestEvaluators, f"test_{evaluator_info['class'].__name__}", test_func)


"""
Response Testing
"""


class TestResponses(unittest.TestCase):
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


"""
Verifier Testing
"""


class TestLocationVerifier(unittest.TestCase):
    def test_valid_locations(self):
        valid_test_cases = [
            "90210",
            "san francisco",
            "san francisco ca",
            "new york",
            "00000",
        ]
        for location in valid_test_cases:
            with self.subTest(location=location):
                verifier = LocationVerifier(location)
                self.assertTrue(verifier.verify(), f"Expected {location} to be valid")

    def test_invalid_locations(self):
        invalid_test_cases = [
            "000000",
            "0000",
            "$@^^$()",
            None,
        ]
        for location in invalid_test_cases:
            with self.subTest(location=location):
                verifier = LocationVerifier(location)
                self.assertFalse(
                    verifier.verify(), f"Expected {location} to be invalid"
                )


class TestApiVerifier(unittest.TestCase):
    def test_valid_api_key(self):
        verifier = ApiKeyVerifier("1234567890ABCDEFGHIJKLMNOPQRSTUV")
        self.assertTrue(verifier.verify())

    def test_invalid_characters(self):
        verifier = ApiKeyVerifier("1234567890ABC!@#XYZ")
        self.assertFalse(verifier.verify())

    def test_invalid_length_short(self):
        verifier = ApiKeyVerifier("12345")
        self.assertFalse(verifier.verify())

    def test_invalid_length_long(self):
        verifier = ApiKeyVerifier("123456789012345678901234567890123")
        self.assertFalse(verifier.verify())

    def test_not_just_numbers(self):
        verifier = ApiKeyVerifier("12345678901234567890123456789012")
        self.assertFalse(verifier.verify())

    def test_empty_string(self):
        verifier = ApiKeyVerifier("")
        self.assertFalse(verifier.verify())

    def test_null_string(self):
        verifier = ApiKeyVerifier(None)
        self.assertFalse(verifier.verify())


"""
Helper Testing
"""


class TestHelpers(unittest.TestCase):
    def test_find_score(self):
        score_ranges = [
            ((45, 50.99), 2),
            ((51, 60.99), 5),
            ((61, 65.99), 6),
            ((66, 70.99), 8),
            ((71, 79.99), 10),
            ((80, 83.99), 9),
            ((84, 86.99), 6),
            ((87, 93.99), 3),
        ]

        evaluator = Evaluator()
        values = generate_floats(150, 10000)

        for value in values:
            with self.subTest(value=value):
                actual_score = evaluator.find_score(score_ranges, value)
                expected_score = find_expected_score(score_ranges, value)

                self.assertEqual(
                    actual_score,
                    expected_score,
                    f"For value {value}, expected {expected_score}, but got {actual_score}",
                )


# loops through the EVALUATORS and tests each one
for evaluator_info in EVALUATORS:
    test_func = lambda self, e=evaluator_info: self.evaluator_test(e["class"])
    setattr(TestEvaluators, f"test_{evaluator_info['class'].__name__}", test_func)


# helpers
def generate_floats(max_num, num_amount):
    return [round(random.uniform(0, max_num), 2) for _ in range(num_amount)]


def find_expected_score(score_ranges, value):
    for (min_val, max_val), score in score_ranges:
        if min_val <= value <= max_val:
            return score
    return 1


if __name__ == "__main__":
    unittest.main()
