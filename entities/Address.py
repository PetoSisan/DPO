from entities.Entity import Entity


class Address(Entity):
    """Class representing address of an building in real world."""

    def __init__(
        self,
        street: str,
        building_number: str,
        postal_code: int | None,
        city: str,
        county="",
        country="",
    ):
        self.street = street
        self.building_number = building_number
        self.postal_code = postal_code
        self.city = city
        self.county = county
        self.country = country

        optional_params = {"required", "county", "country"}
        self.required = self.__dict__.keys() - optional_params

    def to_string(self) -> str:
        """Returns string representation of an `Address` object.

        Params:
            - self (`Address`)
        Returns:
           - (`str`): returns string representation of an `Address` object
        """
        return f"{self.street} {self.building_number}, {self.postal_code} {self.city}"
