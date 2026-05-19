from form import Question

from UI.GUI.views.View import View
from typing import Callable

from form.Question import Question

class QuestionView(View):
    def __init__(self, q: Question, send_answers: Callable[[list[str]], None]):
        super().__init__("start.ui")
        self.question = q
        self.send_answers = send_answers