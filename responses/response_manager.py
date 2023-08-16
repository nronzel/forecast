class ResponseManager:
    # gpt generated responses for now..
    RESPONSES = {
        (0, 1.99): "Golf today? Might as well play Russian roulette.",
        (2, 3.99): "Brave the course today, and your ball isn't the only thing that'll be lost.",
        (4, 5.99): "Golfing today is like playing on hard mode. Good luck.",
        (6, 7.99): "The course might just play you today.",
        (8, 9.99): "Decent conditions, but don't be surprised if the wind betrays you.",
        (10, 10.99): "Nature's indifferent today. Your swing? That's on you.",
    }

    def get_response(self, score):
        # print(score)
        for (low, high), response in self.RESPONSES.items():
            if low <= score <= high:
                return response
        return "couldn't determine weather condition"
