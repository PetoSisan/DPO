from form.Question import Question
from form.FormState import FormState

Answer = str

class Form:
    def __init__(self, start: Question):
        self.start = start
        self.qna: dict[str, list[Answer]] = {}
        self.state = FormState.NOT_STARTED
    