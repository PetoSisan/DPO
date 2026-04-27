from __future__ import annotations # forward references for self-referential data structures

class Question:
    def __init__(self, title: str, row_name: str, answers: dict[str, Question | None], multiple_choice: bool):
        self.title = title
        self.row_name = row_name
        self.answers = answers
        self.multiple_choice = multiple_choice


    def next(self, answer: str) -> Question | None:
        return self.answers.get(answer)