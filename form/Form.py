from form.Question import Question
from form.FormState import FormState

Answer = str

class Form:
    def __init__(self, start: Question):
        self.questions: list[Question | None] = [start]
        self.answers: dict[str, list[Answer]] = {}
        self.state = FormState.NOT_STARTED
        self.current = 0
    

    def get_current(self) -> Question | None:
        return self.questions[self.current]


    def push(self, answers: list[Answer]) -> None:
        """Entry requirements:
            1. There is at least 1 answer in `answers`.
            2. All answers in `answers` have to be equivalent regarding the call of a method `next()`
               on `Question` object.
        """
        assert len(answers) != 0

        curr_question = self.get_current() 
        if curr_question.are_equivalent_answers(self.answers.get(curr_question.row_name, []), answers):
            self.current += 1
            return
        
        self.answers[self.curr_question.row_name] = answers

        self.questions = self.questions[0:self.current]
        self.questions.append( self.curr_question.next(answers[0]) )


    def step_back(self) -> bool:
        if len(self.questions) > 0:
            self.current -= 1
            return True
        return False


    def data(self) -> dict[str, list[Answer]]:
        return self.answers