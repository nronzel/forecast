class Evaluator:
    def evaluate(self):
        raise NotImplementedError


class TempEvaluator(Evaluator):
    def __init__(self, temp):
        self.temp = temp

    def evaluate(self):
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

        if self.temp >= 87:
            return 1

        if self.temp <= 47:
            return 1


