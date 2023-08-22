from .evaluator import Evaluator


class TempEvaluator(Evaluator):
    def __init__(self, temp: float):
        self.temp = temp
        self.scoring_ranges = [
            ((32.00, 50.00), 2),  # Very cold
            ((50.01, 60.00), 4),  # Cold
            ((60.01, 68.00), 6),  # Cool
            ((68.01, 77.00), 10),  # Comfortable
            ((77.01, 85.00), 6),  # Warm
            ((85.01, 95.00), 3),  # Hot
            ((95.01, 105.00), 2),  # Very hot
            ((105.01, 120.00), 1),  # Extremely hot
        ]

    def evaluate(self):
        return self.find_score(self.scoring_ranges, self.temp)


class FeelsLikeEvaluator(Evaluator):
    def __init__(self, feels_like: float):
        self.feels_like = feels_like
        self.scoring_ranges = [
            ((32.00, 50.00), 2),  # Very cold
            ((50.01, 60.00), 4),  # Cold
            ((60.01, 68.00), 6),  # Cool
            ((68.01, 77.00), 10),  # Comfortable
            ((77.01, 85.00), 6),  # Warm
            ((85.01, 95.00), 3),  # Hot
            ((95.01, 105.00), 2),  # Very hot
            ((105.01, 120.00), 1),  # Extremely hot
        ]

    def evaluate(self):
        return self.find_score(self.scoring_ranges, self.feels_like)


class HumidityEvaluator(Evaluator):
    def __init__(self, humidity: float):
        self.humidity = humidity
        self.scoring_ranges = [
            ((0.00, 20.00), 2),  # Extremely dry
            ((20.01, 30.00), 5),  # Dry
            ((30.01, 60.00), 10),  # Comfortable
            ((60.01, 70.00), 7),  # Slightly humid
            ((70.01, 80.00), 4),  # Humid
            ((80.01, 90.00), 3),  # Very humid
            ((90.01, 100.00), 1),  # Extremely humid
        ]

    def evaluate(self):
        return self.find_score(self.scoring_ranges, self.humidity)


class UvEvaluator(Evaluator):
    def __init__(self, uv: float):
        self.uv = uv
        self.scoring_ranges = [
            ((0, 2), 10),  # Low danger
            ((2.01, 5), 8),  # Moderate risk
            ((5.01, 7), 6),  # High risk
            ((7.01, 10), 4),  # Very high risk
            ((10.01, 15), 2),  # Extreme risk
        ]

    def evaluate(self):
        return self.find_score(self.scoring_ranges, self.uv)


class WindEvaluator(Evaluator):
    def __init__(self, wind):
        self.wind = wind
        self.scoring_ranges = [
            ((0, 5), 10),  # Little to no impact
            ((5.01, 12), 8),  # Some adjustments needed
            ((12.01, 20), 6),  # Noticeable impact
            ((20.01, 29), 4),  # Challenging conditions
            ((29.01, 40), 1),  # Extremely challenging
        ]

    def evaluate(self):
        return self.find_score(self.scoring_ranges, self.wind)


class GustEvaluator(Evaluator):
    def __init__(self, gust: float):
        self.gust = gust
        self.scoring_ranges = [
            ((0, 7), 10),  # Little to no impact
            ((7.01, 15), 8),  # Some adjustments needed
            ((15.01, 25), 6),  # Noticeable impact
            ((25.01, 35), 4),  # Challenging conditions
            ((35.01, 50), 2),  # Extremely challenging
        ]

    def evaluate(self):
        return self.find_score(self.scoring_ranges, self.gust)


class RainEvaluator(Evaluator):
    def __init__(self, rain_chance: float):
        self.rain_chance = rain_chance
        self.scoring_ranges = [
            ((0, 10), 10),  # Almost no chance of rain
            ((10.01, 20), 9),  # Very slight chance of rain
            ((20.01, 30), 8),  # Slight chance of rain
            ((30.01, 40), 7),  # Possible light showers
            ((40.01, 50), 6),  # Moderate chance of rain
            ((50.01, 60), 5),  # Expect some rain
            ((60.01, 70), 4),  # Rain likely
            ((70.01, 80), 3),  # Heavy rain expected
            ((80.01, 90), 2),  # Very high chance of heavy rain
            ((90.01, 100), 1),  # Almost certain heavy rain
        ]

    def evaluate(self):
        return self.find_score(self.scoring_ranges, self.rain_chance)


class SnowEvaluator(Evaluator):
    def __init__(self, snow_chance: float):
        self.snow_chance = snow_chance
        self.scoring_ranges = [
            ((0, 10), 10),  # Almost no chance of snow
            ((10.01, 20), 9),  # Very slight chance of snow
            ((20.01, 30), 8),  # Slight chance of snow
            ((30.01, 40), 7),  # Possible light snow
            ((40.01, 50), 6),  # Moderate chance of snow
            ((50.01, 60), 5),  # Expect some snow
            ((60.01, 70), 4),  # Snow likely
            ((70.01, 80), 3),  # Heavy snow expected
            ((80.01, 90), 2),  # Very high chance of heavy snow
            ((90.01, 100), 1),  # Almost certain heavy snow
        ]

    def evaluate(self):
        return self.find_score(self.scoring_ranges, self.snow_chance)


class ConditionEvaluator(Evaluator):
    # evaluates the worst conditions from the global evaluators from each
    # weather category.
    def __init__(self, tf_eval, cur_eval, hour_eval):
        self.todays_forecast_evaluator = tf_eval
        self.current_weather_evaluator = cur_eval
        self.hourly_weather_evaluator = hour_eval

    def evaluate(self):
        all_worst_conditions = {}
        lowest_score = float("inf")  # Initialize to a high value

        # Collect all worst conditions from individual evaluators
        for evaluator in [
            self.todays_forecast_evaluator,
            self.current_weather_evaluator,
            self.hourly_weather_evaluator,
        ]:
            worst_conditions = evaluator.find_worst_conditions()

            for condition, score in worst_conditions.items():
                if condition not in all_worst_conditions:
                    all_worst_conditions[condition] = {
                        "score": score,
                        "counter": 1,
                    }
                else:
                    all_worst_conditions[condition]["counter"] += 1
                    all_worst_conditions[condition]["score"] = min(
                        all_worst_conditions[condition]["score"], score
                    )

                # Update the lowest score if necessary
                lowest_score = min(lowest_score, score)

        # Filter out conditions that do not have the lowest score
        final_worst_conditions = {
            condition: details
            for condition, details in all_worst_conditions.items()
            if details["score"] == lowest_score
        }

        return final_worst_conditions

    def filter_worst_conditions(self, all_worst_conditions):
        # Find the highest occurrence count
        highest_occurrence = max(
            details["counter"] for details in all_worst_conditions.values()
        )

        # Filter the conditions with the highest occurrence count
        filtered_conditions = {
            condition: details["score"]
            for condition, details in all_worst_conditions.items()
            if details["counter"] == highest_occurrence
        }

        # If needed, find the worst score among those with the highest occurrence
        worst_score_among_highest_occurrence = min(filtered_conditions.values())

        # Further filter by worst score if necessary
        final_filtered_conditions = {
            condition: score
            for condition, score in filtered_conditions.items()
            if score == worst_score_among_highest_occurrence
        }

        return final_filtered_conditions
