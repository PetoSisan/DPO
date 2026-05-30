from typing import Callable
from form.Question import Question
from form.Form import Form

from form.FormState import FormState


class Messenger:
    def __init__(
        self,
        form: Form,
        quit: Callable[[], None],
        new_view: Callable[[], None] | None = None,
    ):
        self.form = form
        self.new_view = new_view
        self.quit_callback = quit

    def get_question(self) -> Question | None:
        return self.form.get_current_question()

    def add_answers(self, answers: list[str]) -> None:
        self.form.add_answers(answers)
        self.form.next_question(answers)
        self.new_view()

    def register_callback(self, new_view: Callable[[], None]) -> None:
        self.new_view = new_view

    def summary(self) -> dict[str, list[str]]:
        return self.form.get_qna()

    def quit(self, state: FormState) -> None:
        self.form.set_state(state)
        return self.quit_callback()
