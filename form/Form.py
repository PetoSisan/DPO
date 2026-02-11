from abc import ABC, abstractmethod
from typing import Callable
from .FormState import FormState

from collections import deque

Question = str
Answer = str


class IForm(ABC):
    """Interface (although it probably is not an interface in the true sense
       of the word because of implementing some methods)
       for receiving data from a dialog with user.
    """
    def __init__(self, qna: dict[Question, list[Answer]]):
        self.qna = qna
        self.questions = deque(self.qna.keys())
        self.observer: Callable[[dict[Question, list[Answer]], FormState], bool] | None = None
        self.state = FormState.NOT_STARTED
    

    @abstractmethod
    def run(self) -> None:
        pass
    

    def add_answers(self, question: str, answers: list[str]) -> None:
        self.qna[question] = answers


    def register_callback(self, f: Callable[[dict[Question, list[Answer]], FormState], bool]) -> None:
        self.observer = f


    def call_callback(self) -> bool:
        return self.observer(self.qna, self.state)