from form import Question

from UI.GUI.views.View import View
from typing import Callable

from form.Question import Question

from abc import abstractmethod

class QuestionView(View):
    def __init__(self, design_file: str, q: Question, send_answers: Callable[[list[str]], None]):
        super().__init__(design_file)
        self.question = q
        self.send_answers = send_answers
        self.setup()


    def setup(self) -> None:
        self.ui.question.setText(self.question.title)

        self.clear_placeholders()  
        self.load_answers()
            
    def clear_placeholders(self) -> None:
        while self.ui.gridLayout.count():
            item = self.ui.gridLayout.takeAt(0)

            widget = item.widget()
            if widget:
                widget.deleteLater()
        

    @abstractmethod
    def load_answers(self) -> None:
        pass