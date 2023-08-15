class Evaluator:
    def evaluate(self):
        raise NotImplementedError


class TempEvaluator(Evaluator):
    def __init__(self, temp: int):
        self.temp = temp

    def evaluate(self):
        if 51 <= self.temp <= 59:
            return 4

        if 60 <= self.temp <= 65:
            return 7

        if 66 <= self.temp <= 70:
            return 8

        if 71 <= self.temp <= 75:
            return 10

        if 76 <= self.temp <= 80:
            return 9

        if 81 <= self.temp <= 85:
            return 7

        if 86 <= self.temp <= 92:
            return 3

        if self.temp >= 93:
            return 1

        if self.temp <= 50:
            return 1


class FeelsLikeEvaluator(Evaluator):
    def __init__(self, feels_like: int):
        self.feels_like = feels_like

    def evaluate(self):
        if self.feels_like >= 100:
            return 1

        if self.feels_like <= 45:
            return 1

        if 70 <= self.feels_like <= 79:
            return 10

        if 80 <= self.feels_like <= 85:
            return 8

        if 60 <= self.feels_like <= 69:
            return 7

        if 50 <= self.feels_like <= 59:
            return 4

        return 3


class HumidityEvaluator(Evaluator):
    def __init__(self, humidity):
        self.humidity = humidity

    def evaluate(self):
        if self.humidity >= 90:
            return 1

        if 0 <= self.humidity <= 10:
            return 10

        if 11 <= self.humidity <= 40:
            return 8

        if 41 <= self.humidity <= 50:
            return 5

        if 51 <= self.humidity <= 70:
            return 3

        return 1


class UvEvaluator(Evaluator):
    def __init__(self, uv: int):
        self.uv = uv

    def evaluate(self):
        if self.uv >= 9:
            return 1

        if self.uv <= 1:
            return 10

        if 2 <= self.uv <= 4:
            return 8

        if 5 <= self.uv <= 7:
            return 5

        if self.uv == 8:
            return 3


class WindEvaluator(Evaluator):
    def self__init__(self, wind: float):
        self.wind = wind

    def evaluate(self):
        if self.wind <= 2.0:
            return 10

        if self.wind >= 20.0:
            return 1

        if self.wind <= 5.0:
            return 8

        if 5.0 < self.wind <= 8.0:
            return 6

        if 8.0 < self.wind <= 14.0:
            return 4

        return 3


class GustEvaluator(Evaluator):
    def __init__(self, gust: float):
        self.gust = gust

    def evaluate(self):
        if self.gust >= 25.0:
            return 1

        if self.gust <= 5.0:
            return 10

        if 5.0 < self.gust <= 7.0:
            return 6

        if 7.0 < self.gust <= 12.0:
            return 4

        return 3
