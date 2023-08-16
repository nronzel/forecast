class Evaluator:
    def evaluate(self):
        raise NotImplementedError

    def find_score(self, list, value):
        for (min, max), score in list:
            if min <= value <= max:
                return score
        return 1


class TempEvaluator(Evaluator):
    def __init__(self, temp):
        self.temp = temp
        self.scoring_ranges = [
            ((45, 50.99), 2),
            ((51, 60.99), 5),
            ((61, 65.99), 6),
            ((66, 70.99), 8),
            ((71, 79.99), 10),
            ((80, 83.99), 9),
            ((84, 86.99), 6),
            ((87, 93.99), 3),
        ]

    def evaluate(self):
        return self.find_score(self.scoring_ranges, self.temp)


class FeelsLikeEvaluator(Evaluator):
    def __init__(self, feels_like):
        self.feels_like = feels_like
        self.scoring_ranges = [
            ((45, 50.99), 2),
            ((51, 60.99), 5),
            ((61, 65.99), 6),
            ((66, 70.99), 8),
            ((71, 79.99), 10),
            ((80, 83.99), 9),
            ((84, 86.99), 6),
            ((87, 95.99), 3),
        ]

    def evaluate(self):
        return self.find_score(self.scoring_ranges, self.feels_like)


class HumidityEvaluator(Evaluator):
    def __init__(self, humidity: float):
        self.humidity = humidity
        self.scoring_ranges = [
            ((0, 10.99), 10),
            ((10, 40.99), 8),
            ((41, 50.99), 5),
            ((51, 70.99), 3),
            ((71, 85.99), 2),
        ]

    def evaluate(self):
        return self.find_score(self.scoring_ranges, self.humidity)


class UvEvaluator(Evaluator):
    def __init__(self, uv: int):
        self.uv = uv
        self.scoring_ranges = [
            ((0, 1), 10),
            ((2, 4), 8),
            ((5, 7), 5),
            ((8, 8), 3),
        ]

    def evaluate(self):
        return self.find_score(self.scoring_ranges, self.uv)


class WindEvaluator(Evaluator):
    def __init__(self, wind):
        self.wind = wind
        self.scoring_ranges = [
            ((0, 2.99), 10),
            ((3, 5.99), 8),
            ((6, 8.99), 6),
            ((9, 14.99), 4),
        ]

    def evaluate(self):
        return self.find_score(self.scoring_ranges, self.wind)


class GustEvaluator(Evaluator):
    def __init__(self, gust: float):
        self.gust = gust
        self.scoring_ranges = [
            ((0, 5.99), 10),
            ((6, 8.99), 8),
            ((9, 12.99), 5),
            ((13, 17.99), 4),
            ((18, 23.99), 2),
        ]

    def evaluate(self):
        return self.find_score(self.scoring_ranges, self.gust)
