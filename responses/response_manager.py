class ResponseManager:
    RESPONSES = {
        range(9, 11): "GREAT DAY FOR GOLF",
    }

    def get_response(self, score):
        for score_range, response in self.RESPONSES.items():
            if score in score_range:
                return response
        return "couldn't determine the weather condition"
