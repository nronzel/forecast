class ResponseManager:
    # TODO - actual responses
    RESPONSES = {
        (0, 1.99): "Don't go outside",
        (2, 3.99): "2 or 3",
        (4, 5.99): "4 or 5",
        (6, 7.99): "6 or 7",
        (8, 9.99): "8 or 9",
        (10, 10.99): "Perfect day!",
    }

    def get_response(self, score):
        print(score)
        for (low, high), response in self.RESPONSES.items():
            if low <= score <= high:
                return response
        return "couldn't determine weather condition"
