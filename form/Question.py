from __future__ import annotations # forward references for self-referential data structures

class Question:
    def __init__(self, title: str, row_name: str, answers: dict[str, Question | None]):
        self.title = title
        self.row_name = row_name
        self.answers = answers

    def next(self, answer: str) -> Question | None:
        return self.answers.get(answer)