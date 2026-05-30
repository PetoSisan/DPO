from entities.Address import Address
from entities.Person import Person


class PhysicalPerson(Person):
    def __init__(
        self,
        title: str = "",
        name: str = "",
        surname: str = "",
        address: Address | None = None,
        phone: str = "",
        mail: str = "",
    ):
        super().__init__(name, address, phone, mail)
        self.title = title
        self.surname = surname

        self.required = self.__dict__.keys() - {"required", "title"}

    def get_full_name(self) -> str:
        return f"{self.name} {self.surname}"

    def to_string(self) -> str:
        address = self.address.to_string() if self.address is not None else ""
        title = self.title
        if len(self.title) != 0:
            title += " "
        return f"""{self.title}{self.get_full_name()}
{self.format_attribute("Adresa", address)}
{self.format_attribute("Tel. číslo", self.phone)}
{self.format_attribute("Email", self.mail)}"""
