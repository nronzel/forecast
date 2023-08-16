import unittest
import random

from responses.response_manager import ResponseManager


def generate_floats(n):
    return [round(random.uniform(0, 10), 2) for _ in range(n)]


class Tests(unittest.TestCase):
    def test_response_manager_responses(self):
        rm = ResponseManager()
        test_scores = generate_floats(100)

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
                        f"curr score {score}, expected '{expected_response}' but got '{response}'",
                    )
                    break


if __name__ == "__main__":
    unittest.main()
