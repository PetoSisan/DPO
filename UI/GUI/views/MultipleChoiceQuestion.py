from UI.GUI.views.QuestionView import QuestionView
from form.Question import Question

from typing import Callable

class MultipleChoiceQuestionView(QuestionView):
    def __init__(self, q: Question, send_answers: Callable[[list[str]], None]):
        super().__init__("multiple_choice_question.ui", q, send_answers)