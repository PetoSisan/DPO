from form.Question import Question
from form.FormState import FormState

Answer = str

class Form:
    def __init__(self, start: Question):
        self.current: Question | None = start
        self.qna: dict[str, list[Answer]] = {}
        self.state = FormState.NOT_STARTED
    

    def add_answers(self, answers: list[str]) -> None:
        self.qna[self.current.row_name] = answers


    def get_current_question(self) -> Question | None:
        return self.current
    

    def next_question(self) -> Question | None:
        self.current = self.current.next()
        return self.current
    