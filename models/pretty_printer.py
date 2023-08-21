class PrettyPrinter:
    def __init__(self, weather, worst_conditions):
        self.weather = weather
        self.worst_conditions = worst_conditions
        self.todays_score = self.weather.todays_forecast_evaluator.evaluate()
        self.current_weather_score = self.weather.current_weather_evaluator.evaluate()
        self.hourly_score = self.weather.hourly_weather_evaluator.evaluate()

    def get_todays_forecast(self):
        return self.weather.parser.parsed_weather_data["todays_forecast"]

    def print(self):
        self.print_header("Location Data")
        self.print_location_data()
        self.print_footer()

        self.print_header("Today's Forecast")
        self.print_todays_condition()
        self.print_todays_forecast()
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
        location_data = self.weather.get_location_data()
        for key, value in location_data.items():
            print("| {:<15} : {:>20} |".format(key.capitalize(), value))

    def print_todays_condition(self):
        print("|{:^40}|".format(self.weather.get_todays_condition()))

    def print_todays_forecast(self):
        forecast = self.get_todays_forecast()
        for key, value in forecast.items():
            # skip listing the condition, we're already printing it
            if key == "condition":
                continue
            print("| {:<15} : {:>20} |".format(key.capitalize(), value))

    def get_total_score(self):
        return self.weather.evaluate_conditions()

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
        print(
            "| Average Score          : {:>13} |".format(
                self.weather.evaluate_conditions()
            )
        )

    def print_worst_conditions(self):
        filtered_worst_conditions = self.weather.filter_worst_conditions(
            self.worst_conditions
        )
        for condition, score in filtered_worst_conditions.items():
            print("| {:<15} : {:>20} |".format(condition, score))
