from abc import ABC, abstractmethod
from .FormState import FormState

from collections import deque

from form.Form import Form

Question = str
Answer = str


class IFormManager(ABC):
    """Interface (although it probably is not an interface in the true sense
       of the word because of implementing some methods)
       for receiving data from a dialog with user.
    """
    def __init__(self, form: Form):
        self.form = form
    

    @abstractmethod
    def run(self) -> None:
        pass

    def wanted(self) -> bool:
        """Checks whether user wants to fill the form.
        Params:
        
        Returns:
            `True`, if yes, `False` otherwise
        """

        answer: str = input("Prajete si vypĺňať 'Vyjadrenie' k žiadosti DPO? [ano/nie] \n")
        return True if answer.lower() == "ano" else False
    

    def add_answers(self, question: str, answers: list[str]) -> None:
        self.form.add_answers(question, answers)


    def next_question(self) -> Question | None:
        return self.form.next_question()