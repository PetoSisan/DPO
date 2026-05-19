from __future__ import annotations # forward references for self-referential data structures

from abc import ABC


class Question(ABC):
    def __init__(self, title: str, row_name: str, answers: dict[str, Question | None]):
        self.title = title
        self.row_name = row_name
        self.answers = answers


    def next(self, answer: str) -> Question | None:
        return self.answers.get(answer)

    
    def are_equivalent_answers(self, answers: list[str]) -> bool:
        if len(answers) == 0:
            return True

        next = self.next(answers[0])

        for i in range(1, len(answers)):
            if next != self.next(answers[i]):
                return False
        
        return True