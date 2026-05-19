from UI.GUI.views.QuestionView import QuestionView
from form.Question import Question

from typing import Callable

class SingleChoiceQuestionView(QuestionView):
    def __init__(self, q: Question, send_answers: Callable[[list[str]], None]):
        super().__init__("single_choice_question.ui", q, send_answers)