from UI.GUI.views.QuestionView import QuestionView
from form.Question import Question

from typing import Callable

from PySide6.QtWidgets import QRadioButton

class SingleChoiceQuestionView(QuestionView):
    def __init__(self, q: Question, send_answers: Callable[[list[str]], None]):
        super().__init__("single_choice_question.ui", q, send_answers)

    def load_answers(self):
        # Add new radio buttons from data
        for row, answer in enumerate(self.question.answers.keys()):
            radio_button = QRadioButton(answer)
            self.ui.gridLayout.addWidget(radio_button, row, 0)