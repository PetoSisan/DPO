from form.FormState import FormState
from form.Question import Question

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

    def set_current_question(self, q: Question) -> None:
        self.current = q

    def set_state(self, state: FormState) -> None:
        self.state = state

    def get_qna(self) -> dict[str, list[Answer]]:
        return self.qna

    def next_question(self, answers: list[str]) -> None:
        assert len(answers) > 0 and \
            self.current.are_equivalent_answers(answers)

        self.current = self.current.next(answers[0])
        return self.current
