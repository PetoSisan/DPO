from Address import Address
from Person import Person
from PhysicalPerson import PhysicalPerson

class Corporate(Person):
    def __init__(self, person: PhysicalPerson, name: str = "", HQ: Address | None = None, ICO: int | None = None, phone: str = "", mail: str = ""):
        super().__init__(name, HQ, phone, mail)
        self.ICO = ICO
        self.person = person

        self.required.add(self.ICO)
        self.required.add(self.person)
        self.person.required = {self.person.name, self.person.surname}
    
    def get_full_name(self) -> str:
        return self.name
    
    def to_string(self) -> str:
        address = self.address.to_string() if self.address is not None else ""
        person = self.person.to_string() if self.person is not None else ""
        
        return f"""{self.get_full_name()}
{self.format_attribute("Adresa", address)}
{self.format_attribute("IČO", self.ICO)}
{self.format_attribute("Tel. číslo", self.phone)}
{self.format_attribute("Email", self.mail)}
        
Identifikačné údaje oprávnenej osoby:
    {person}"""