class Parser:
    def __init__(self, raw_data):
        self.parsed_weather_data = None
        self.parsed_location_data = self._parse_location_data(raw_data)

    def parse_weather_data(self):
        return None

    def _parse_location_data(self, raw_data):
        location_data = raw_data["location"]
        parsed_data = {
            "city": location_data["name"],
            "state": location_data["region"],
            "localtime": location_data["localtime"],
        }
        return parsed_data
