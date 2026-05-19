from form.Question import Question

class SingleChoiceQuestion(Question):
    def __init__(self, title, row_name, answers):
        super().__init__(title, row_name, answers)