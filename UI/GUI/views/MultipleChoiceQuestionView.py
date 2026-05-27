from UI.GUI.views.QuestionView import QuestionView
from form.Question import Question

from typing import Callable

from PySide6.QtWidgets import QCheckBox

class MultipleChoiceQuestionView(QuestionView):
    def __init__(self, q: Question, send_answers: Callable[[list[str]], None]):
        super().__init__("multiple_choice_question.ui", q, send_answers)
    

    def load_answers(self):
        # Add new radio buttons from data
        for row, answer in enumerate(self.question.answers.keys()):
            check_box = QCheckBox(answer)
            self.ui.gridLayout.addWidget(check_box, row, 0)