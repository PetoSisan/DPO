from abc import ABC, abstractmethod
from form.FormState import FormState

from collections import deque

from form.Form import Form

Question = str
Answer = str


class UI(ABC):
    """Interface (although it probably is not an interface in the true sense
       of the word because of implementing one method)
       for receiving data from a dialog with user.
    """
    def __init__(self):
        return
    
    def wanted(self) -> bool:
        """Checks whether user wants to fill the form.
        Params:
        
        Returns:
            `True`, if yes, `False` otherwise
        """

        answer: str = input("Prajete si vypĺňať 'Vyjadrenie' k žiadosti DPO? [ano/nie] \n")
        return True if answer.lower() == "ano" else False

    @abstractmethod
    def run(self, form: Form, project_id: str) -> None:
        pass

    @abstractmethod
    def quit(self) -> None:
        pass