from entities.FacilityPart import FacilityPart

class Facility:
    """Class representing facility / construction."""
    def __init__(self, code: str = "", title: str = "",
                 construction_class: str = "",
                 parts: list[FacilityPart] = []):
        self.code = code
        self.title = title
        self.construction_class = construction_class
        self.parts = parts
    
    def format(self) -> str:
        """Creates a formatted `str` representation of an facility.
        
        Params:
            - self (`Facility`)
        
        Returns:
            - (`str`): a formatted `str` representation of an facility
        """
        result = ""
        if self.code != "" and self.title != "":
            result += f"{self.code}, {self.title}\n"

        header_1 = 13 # Kód stavebného objektu
        header_2 = len("Názov stavebného objektu") + 5 # Názov stavebného objektu

        for part in self.parts:
            result += f"{part.code:<{header_1}} | {part.title:<{header_2}} \n"

        return result