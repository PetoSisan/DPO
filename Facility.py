from FacilityPart import FacilityPart

class Facility:
    def __init__(self, code: str = "", title: str = "", construction_class: str = "", parts: list[FacilityPart] = []):
        self.code = code
        self.title = title
        self.construction_class = construction_class
        self.parts = parts