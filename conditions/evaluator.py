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

    def get_evaluators(self):
        raise NotImplementedError

    def find_worst_conditions(self):
        worst_conditions = {}

        for evaluator in self.get_evaluators():
            score = evaluator.evaluate()
            condition_name = type(evaluator).__name__.replace("Evaluator", "")

            if condition_name not in worst_conditions:
                worst_conditions[condition_name] = {"score": score, "counter": 1}
            else:
                worst_conditions[condition_name]["counter"] += 1
                worst_conditions[condition_name]["score"] = min(
                    worst_conditions[condition_name]["score"], score
                )

        return worst_conditions
