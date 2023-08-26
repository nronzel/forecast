import statistics


class Evaluator:
    def evaluate(self):
        raise NotImplementedError

    def find_score(self, list, value):
        for (min, max), score in list:
            if min <= value <= max:
                return score
        return 1


class GlobalEvaluator:
    def __init__(self, data):
        self.data = data

    def evaluate(self):
        total_score = 0
        num_evaluators = 0
        for evaluator in self.get_evaluators():
            total_score += evaluator.evaluate()
            num_evaluators += 1
        return round(total_score / num_evaluators) if num_evaluators else 0

    def get_median_score(self):
        scores = [evaluator.evaluate() for evaluator in self.get_evaluators()]
        return statistics.median(scores)

    def get_evaluators(self):
        raise NotImplementedError

    def find_worst_conditions(self):
        worst_score = float("inf")
        worst_conditions = {}

        for evaluator in self.get_evaluators():
            score = evaluator.evaluate()
            condition_name = type(evaluator).__name__.replace("Evaluator", "")

            if score < worst_score:
                worst_score = score
                worst_conditions = {condition_name: score}
            elif score == worst_score:
                worst_conditions[condition_name] = score

        return worst_conditions
