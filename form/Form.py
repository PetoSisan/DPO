from form.Question import Question

Answer = str

class Form:
    def __init__(self, start: Question):
        self.start = start
        self.qna: dict[str, list[Answer]] = {}
    