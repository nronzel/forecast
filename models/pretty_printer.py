class PrettyPrinter:
    def __init__(self, weather, worst_conditions):
        self.weather = weather
        self.worst_conditions = worst_conditions
        self.todays_score = self.weather.todays_forecast_evaluator.evaluate()
        self.current_weather_score = self.weather.current_weather_evaluator.evaluate()
        self.hourly_score = self.weather.hourly_weather_evaluator.evaluate()

    def print(self):
        self.print_header("Location Data")
        self.print_location_data()
        self.print_footer()

        self.print_header("Today's Forecast")
        self.print_todays_condition()
        self.print_footer()

        self.print_header("Weather Scores")
        self.print_weather_scores()
        self.print_footer()

        self.print_header("What Sucks Today")
        self.print_worst_conditions()
        self.print_footer()

    def print_header(self, title):
        print("+" + "-" * 40 + "+")
        print("|{:^40}|".format(f" ~~{title}~~ "))

    def print_footer(self):
        print("+" + "-" * 40 + "+")

    def print_location_data(self):
        for key, value in self.weather.location_data.items():
            print("| {:<15} : {:>20} |".format(key.capitalize(), value))

    def print_todays_condition(self):
        print("|{:^40}|".format(self.weather.todays_condition))

    def get_total_score(self):
        sum = self.todays_score + self.current_weather_score + self.hourly_score
        average = round(sum / 3)
        return average

    def print_weather_scores(self):
        print(
            "| Today's Forecast Score : {:>13} |".format(
                self.weather.todays_forecast_evaluator.evaluate()
            )
        )
        print(
            "| Current Weather Score  : {:>13} |".format(
                self.weather.current_weather_evaluator.evaluate()
            )
        )
        print(
            "| Hourly Weather Score   : {:>13} |".format(
                self.weather.hourly_weather_evaluator.evaluate()
            )
        )
        print("| Average Score          : {:>13} |".format(self.get_total_score()))

    def print_worst_conditions(self):
        filtered_worst_conditions = self.weather.filter_worst_conditions(
            self.worst_conditions
        )
        for condition, score in filtered_worst_conditions.items():
            print("| {:<15} : {:>20} |".format(condition, score))
