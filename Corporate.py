from Address import Address
from Person import Person
from PhysicalPerson import PhysicalPerson

class Corporate(Person):
    """Class representing PO (== právnická osoba == legal entity).
    Yeah I know, that corporates are not the only type of legal entities. I will fix it later."""
    def __init__(self, person: PhysicalPerson, name: str = "", HQ: Address | None = None, ICO: int | None = None, phone: str = "", mail: str = ""):
        super().__init__(name, HQ, phone, mail)
        self.ICO = ICO
        self.person = person

        self.required = self.__dict__.keys() - {"required"}
        self.person.required = {"name", "surname"}
    
    def get_full_name(self) -> str:
        """ Gets the name of PO.
        Params:
            - `self` (`Corporate`)
        Returns:
            - (`str`): name of the PO             
        """
        return self.name
    
    def to_string(self) -> str:
        """Returns string representation of an `Corporate` object.
        
        Params:
            - self (`Corporate`)
        Returns:
            - (`str`): returns string representation of an `Corporate` object
        """
        address = self.address.to_string() if self.address is not None else ""
        person = self.person.to_string() if self.person is not None else ""
        
        return f"""{self.get_full_name()}
{self.format_attribute("Adresa", address)}
{self.format_attribute("IČO", self.ICO)}
{self.format_attribute("Tel. číslo", self.phone)}
{self.format_attribute("Email", self.mail)}
        
Identifikačné údaje oprávnenej osoby:
    {person}"""