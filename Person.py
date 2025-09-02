from abc import ABC, abstractmethod

from Address import Address
from Entity import Entity

class Person(Entity):
    def __init__(self, name: str = "", address: Address | None = None, phone: str = "", mail: str = ""):
        self.name = name
        self.address = address
        self.phone = phone
        self.mail = mail
        self.required = {name, address, phone, mail}
    

    def is_complete(self) -> bool:
        return len(self.get_missing_attrs()) == 0 
    

    def is_missing(self, attr) -> bool:
        if (isinstance(attr, Address) or isinstance(attr, Person)):
            return not attr.is_complete()

        return attr is None or len(attr) == 0
            
    
    @abstractmethod
    def get_full_name(self) -> str:
        pass
    
    @abstractmethod
    def to_string(self) -> str:
        pass