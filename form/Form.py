from abc import ABC, abstractmethod
from typing import Callable
from .FormState import FormState

Question = str
Answer = str


class IForm(ABC):
    """Interface (although it probably is not an interface in the true sense
       of the word because of implementing some methods)
       for receiving data from a dialog with user.
    """
    def __init__(self, qna: dict[Question, list[Answer]]):
        self.qna = qna
        self.observers: set[dict[Question, list[Answer]]] = set()
        self.state = FormState.NOT_STARTED
    

    @abstractmethod
    def run(self) -> None:
        pass


    def register_callback(self, f: Callable[ [dict[Question, list[Answer]], FormState], int ]) -> None:
        self.observers.add(f)


    def call_callback(self, received: dict[Question, list[Answer]]) -> int:
        errors = 0

        for f in self.observers:
            errors += f(received, self.state)
        
        return errors
