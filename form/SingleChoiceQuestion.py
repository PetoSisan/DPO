from form.Question import Question


class SingleChoiceQuestion(Question):
    def __init__(
        self,
        title: str,
        row_name: str,
        answers: dict[str, Question | None]
    ):
        super().__init__(title, row_name, answers)
