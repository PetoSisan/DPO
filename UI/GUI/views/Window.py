from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from UI.GUI.views.View import View
from UI.GUI.views.StartView import StartView
from UI.GUI.views.QuestionView import QuestionView

from typing import Callable

from form.Question import Question

from UI.GUI.Messenger import Messenger

class Window(QWidget):
    def __init__(self, messenger: Messenger):
        super().__init__()
        self.messenger = messenger

        self.setWindowTitle("Fomulár k DPO")
        self.resize(1920, 1080)

        self.stack = QStackedWidget()
        self.stack.addWidget(StartView())

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)


    def connect(self) -> None:
        pass

    def create_question_view(self, question: Question) -> None:  
        pass

    def new_view(self) -> None:
        q: Question | None = self.messenger.get_question()
        if q is not None:
            self.create_question_view(q)
        pass
    


    def redirect(self, old: View | None, new: View, msg: str= "") -> None:   
        if old is not None:
            self.stack.removeWidget(old)

        self.stack.addWidget(new)
        self.stack.setCurrentWidget(new)

        if len(msg) != 0:
            new.success(msg)