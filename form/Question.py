from __future__ import annotations # forward references for self-referential data structures

from abc import ABC


class Question(ABC):
    def __init__(self, title: str, row_name: str, answers: dict[str, Question | None]):
        self.title = title
        self.row_name = row_name
        self.answers = answers


    def next(self, answer: str) -> Question | None:
        return self.answers.get(answer)
    
    def are_equivalent_answers(self, old_answers: list[str], new_answers: list[str]) -> bool:
        return len(old_answers) != 0 and len(new_answers) != 0 and \
               self.next(old_answers[0]) == self.next(new_answers[0])