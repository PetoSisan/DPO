from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from GUI.views.View import View
from GUI.views.StartView import StartView
from GUI.views.QuestionView import QuestionView

from typing import Callable

from form.Question import Question

class Window(QWidget):
    def __init__(self, get_question: Callable[[], Question | None],
                 send_answers: Callable[[list[str]], None],
                 submit: Callable[[], None]):
        super().__init__()
        self.get_question = get_question
        self.send_answers = send_answers
        self.submit = submit

        self.setWindowTitle("Fomulár k DPO")
        self.resize(1920, 1080)

        self.stack = QStackedWidget()
        self.stack.addWidget(StartView())

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)


    def connect(self) -> None:
        pass

    def create_question_view(self, question: Question) -> None:  
        view = QuestionView(question)

    def new_view(self) -> Question | None:
        q: Question | None =  self.get_question()
        if q is not None:
            self.create_question_view(q)
    


    def redirect(self, old: View | None, new: View, msg: str= "") -> None:   
        if old is not None:
            self.stack.removeWidget(old)

        self.stack.addWidget(new)
        self.stack.setCurrentWidget(new)

        if len(msg) != 0:
            new.success(msg)