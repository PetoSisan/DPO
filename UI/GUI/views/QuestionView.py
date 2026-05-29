from form import Question

from UI.GUI.views.View import View
from typing import Callable

from form.Question import Question

from abc import abstractmethod

class QuestionView(View):
    def __init__(self, design_file: str, q: Question, callback: Callable[[list[str]], None]):
        super().__init__(design_file)
        self.question = q
        self.callback = callback
        self.setup()
        self.ui.next.clicked.connect(self.send_answers)
        self.ui.prev.hide()


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
        

    def send_answers(self) -> None:
        answers: list[str] = self.collect_answers()

        if len(answers) == 0:
            self.error("Nezadali ste žiadnu odpoveď.")
            return
        
        self.callback(answers)

    @abstractmethod
    def load_answers(self) -> None:
        pass

    def collect_answers(self) -> list[str]:
        answers = []

        for i in range(self.ui.gridLayout.count()):
            widget = self.ui.gridLayout.itemAt(i).widget()
            if widget and widget.isChecked():
                answers.append(widget.text())
        
        return answers
