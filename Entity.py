from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self):
        self.required = set()
    
    def get_missing_attrs(self):
        attrs = []
        required = self.required & self.__dict__.keys()
        for attr in required:
            value = getattr(self, attr)
            if self.is_missing(value):
                 attrs.append(attr)
        
        return attrs
    

    @abstractmethod
    def is_missing(self, attr) -> bool:
        pass