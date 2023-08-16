class Evaluator:
    def evaluate(self):
        raise NotImplementedError

    def find_score(self, list, value):
        for (min, max), score in list:
            if min <= value <= max:
                return score
        return 1


class TempEvaluator(Evaluator):
    def __init__(self, temp: float):
        self.temp = temp
        self.scoring_ranges = [
            ((32.00, 50.00), 2),  # Very cold
            ((50.01, 60.00), 4),  # Cold
            ((60.01, 68.00), 6),  # Cool
            ((68.01, 77.00), 10),  # Comfortable
            ((77.01, 85.00), 6),  # Warm
            ((85.01, 95.00), 4),  # Hot
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
            ((85.01, 95.00), 4),  # Hot
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
            ((70.01, 80.00), 5),  # Humid
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
