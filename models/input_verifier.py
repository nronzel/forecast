import re


class Verifier:
    def verify(self) -> bool:
        raise NotImplementedError


class LocationVerifier(Verifier):
    def __init__(self, location: str):
        self.location = location

    def verify(self) -> bool:
        if self.location is None:
            return False
        return (
            self.is_zip_code(self.location)
            or self.is_city_state(self.location)
            or self.is_city(self.location)
            or self.is_default(self.location)
        )

    @staticmethod
    def is_zip_code(location: str) -> bool:
        # contains only 5 numbers
        return bool(re.fullmatch(r"\d{5}", location))

    @staticmethod
    def is_city_state(location: str) -> bool:
        # any string of chars with a space plus a space with another char string
        return bool(re.fullmatch(r"[a-zA-Z\s]+[,\s]\s*[a-zA-Z\s]+", location))

    @staticmethod
    def is_city(location: str) -> bool:
        # any string of chars that could also contain a space
        return bool(re.fullmatch(r"[a-zA-Z\s]+", location))

    @staticmethod
    def is_default(location: str) -> bool:
        return location == "auto:ip"


class ApiKeyVerifier(Verifier):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def verify(self) -> bool:
        # checks if the api key has length of 32 and contains letter and numbers
        if self.api_key is None:
            return False
        return bool(
            re.fullmatch(r"^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z0-9]{31}$", self.api_key)
        )
