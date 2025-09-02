from Entity import Entity

class Address(Entity):
    def __init__(self, street: str, building_number: str, postal_code: int | None, city: str, county = "", country = ""):
        self.street = street
        self.building_number = building_number
        self.postal_code = postal_code
        self.city = city
        self.county = county
        self.country = country
        
        
        self.required = {self.street, self.building_number, self.postal_code, self.city}
    
    
    def to_string(self) -> str:
        return f"{self.street} {self.building_number} \n{self.postal_code} {self.city}"
    

    def is_complete(self) -> bool:
        return len(self.get_missing_attrs()) == 0
    

    def is_missing(self, attr) -> bool:
        return attr is None or len(attr) == 0