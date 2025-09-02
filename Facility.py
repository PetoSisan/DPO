from FacilityPart import FacilityPart

class Facility:
    def __init__(self, code: str = "", title: str = "", parts: list[FacilityPart] = []):
        self.code = code
        self.title = title
        self.parts = parts