import re


class Verifier:
    def verify(self) -> bool:
        raise NotImplementedError


class LocationVerifier(Verifier):
    def __init__(self, location: str):
        self.location = location

    def verify(self) -> bool:
        if self.is_zip_code(self.location):
            return True
        elif self.is_city_state(self.location):
            return True
        elif self.is_city(self.location):
            return True
        elif self.is_default(self.location):
            return True
        else:
            return False

    @staticmethod
    def is_zip_code(location: str) -> bool:
        return bool(re.fullmatch(r"\d{5}", location))

    @staticmethod
    def is_city_state(location: str) -> bool:
        return bool(re.fullmatch(r"[a-zA-Z\s]+[,\s]\s*[a-zA-Z\s]+", location))

    @staticmethod
    def is_city(location: str) -> bool:
        return bool(re.fullmatch(r"[a-zA-Z\s]+", location))

    @staticmethod
    def is_default(location: str) -> bool:
        return location == "auto:ip"


class ApiKeyVerifier(Verifier):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def verify(self) -> bool:
        return bool(re.fullmatch(r"[a-zA-Z0-9]{32}", self.api_key))
