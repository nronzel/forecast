import re


class Sanitizer:
    def sanitize(self):
        raise NotImplementedError


class LocationSanitizer(Sanitizer):
    def __init__(self, location):
        self.location = location

    def sanitize(self):
        if self.is_zip_code(self.location):
            return "zip_code", self.location
        elif self.is_city_state(self.location):
            return "city_state", self.location
        elif self.is_city(self.location):
            return "city", self.location
        elif self.is_default(self.location):
            return "default", self.location
        else:
            return "invalid", self.location

    @staticmethod
    def is_zip_code(location):
        return bool(re.fullmatch(r"\d{5}", location))

    @staticmethod
    def is_city_state(location):
        return bool(re.fullmatch(r"[a-zA-Z\s]+[,\s]\s*[a-zA-Z\s]+", location))

    @staticmethod
    def is_city(location):
        return bool(re.fullmatch(r"[a-zA-Z\s]+", location))

    @staticmethod
    def is_default(location):
        return location == "auto:ip"


class ApiKeySanitizer(Sanitizer):
    def __init__(self, api_key):
        self.api_key = api_key

    def sanitize(self):
        return bool(re.fullmatch(r"[a-zA-Z0-9]{32}", self.api_key))
