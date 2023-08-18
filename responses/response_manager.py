class ResponseManager:
    RESPONSES = {
        (0, 1.99): "Not today, don't even get out of bed.",
        (2, 3.99): "Brave the course today, and your ball isn't the only thing that'll be lost.",
        (4, 5.99): "Expect some challenges if you golf today..",
        (6, 7.99): "Not the best weather, but golfable.",
        (8, 9.99): "Almost perfect weather for golf, your swing? That's on you..",
        (10, 10.99): "Better call out sick and get the next tee time, weather is perfect!",
    }

    def get_response(self, score):
        # print(score)
        for (low, high), response in self.RESPONSES.items():
            if low <= score <= high:
                return response
        return "couldn't determine weather condition"
