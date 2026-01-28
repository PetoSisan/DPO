from abc import ABC
from typing import Any

class Entity(ABC):
    """Abstract class encasulating work with attributes"""
    def __init__(self):
        self.required = set()
    
    def get_missing_attrs(self) -> list[Any]:
        """"Gets missing (or empty) attributes

        Params:
            - self (`Entity`)

        Returns:
            - (`list[Any]`): list of missing attributes 
           
        """
        attrs = []
        
        for attr in self.required:
            value = getattr(self, attr)
            if self.is_missing(value):
                 attrs.append(attr)
        
        return attrs


    def format_attribute(self, name: str, value: int | str | None) -> str:
        """Formats attribute in following format: '`name`: `value`' if attribute
        has some meaningfull value (`value is not None and value != ""`)

        Params:
            - self (`Entity`)
            - name (`str`): name of the attribute
            - value (`int | str | None`): value of an attribute
        
        Returns:
            - (`str`): formated attribute   
        """
        return f"{name}: {value}" if value is not None and value != "" else ""

    
    def is_complete(self) -> bool:
        """Checks whether current object contain all **required** information.
        
        Params:
            - self (`Entity`)
        
        Returns:
            - (`bool`): `True` if is complete, `False` otherwise 
        """
        return len(self.get_missing_attrs()) == 0

    
    def is_missing(self, attr: Any) -> bool:
        """"Checks wheter attribute is missing.
        
        Params:
            - self (`Entity`)
            - attr (`Any`): attribute of an `Entity`
        
        Returns:
            - (`bool`): `True` if is missing, `False` otherwise
        """
        return attr is None or len(attr) == 0