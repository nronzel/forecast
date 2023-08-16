class ResponseManager:
    RESPONSES = {
        (1, 1): "Don't go outside",
        (2, 3): "2 or 3",
        (4, 5): "4 or 5",
        (6, 7): "6 or 7",
        (8, 9): "8 or 9",
        (10, 10): "Perfect day!",
    }

    def get_response(self, score):
        formatted_score = format(score, ".2f")
        print(formatted_score)

        for (low, high), response in self.RESPONSES.items():
            if low <= score <= high:
                return response
        return "couldn't determine weather condition"
