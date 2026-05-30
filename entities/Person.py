from abc import abstractmethod

from entities.Address import Address
from entities.Entity import Entity


class Person(Entity):
    def __init__(
        self,
        name: str = "",
        address: Address | None = None,
        phone: str = "",
        mail: str = "",
    ):
        self.name = name
        self.address = address
        self.phone = phone
        self.mail = mail
        self.required = self.__dict__.keys()

    def is_missing(self, attr) -> bool:
        if isinstance(attr, Address) or isinstance(attr, Person):
            return not attr.is_complete()

        return attr is None or len(attr) == 0

    @abstractmethod
    def get_full_name(self) -> str:
        pass

    @abstractmethod
    def to_string(self) -> str:
        pass
