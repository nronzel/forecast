from .condition_evaluators import (
    GustEvaluator,
    HumidityEvaluator,
    RainEvaluator,
    TempEvaluator,
    FeelsLikeEvaluator,
    UvEvaluator,
    WindEvaluator,
    SnowEvaluator,
    ConditionEvaluator,
)
from .evaluator import GlobalEvaluator


class TodaysForecastEvaluator(GlobalEvaluator):
    def get_evaluators(self):
        return [
            TempEvaluator(self.data["avg_temp"]),
            WindEvaluator(self.data["max_wind"]),
            HumidityEvaluator(self.data["avg_humidity"]),
            RainEvaluator(self.data["rain_chance"]),
            SnowEvaluator(self.data["snow_chance"]),
            ConditionEvaluator(
                self.data["condition"],
            ),
        ]


class CurrentWeatherEvaluator(GlobalEvaluator):
    def get_evaluators(self):
        return [
            TempEvaluator(self.data["temp"]),
            FeelsLikeEvaluator(self.data["feels_like"]),
            HumidityEvaluator(self.data["humidity"]),
            UvEvaluator(self.data["uv"]),
            WindEvaluator(self.data["wind"]),
            GustEvaluator(self.data["gust"]),
            ConditionEvaluator(self.data["condition"]),
        ]


class HourlyWeatherEvaluator(GlobalEvaluator):
    def get_evaluators(self):
        return [
            TempEvaluator(self.data["temp"]),
            FeelsLikeEvaluator(self.data["feels_like"]),
            HumidityEvaluator(self.data["humidity"]),
            UvEvaluator(self.data["uv"]),
            WindEvaluator(self.data["wind"]),
            GustEvaluator(self.data["gust"]),
            RainEvaluator(self.data["rain_chance"]),
            SnowEvaluator(self.data["snow_chance"]),
        ]
