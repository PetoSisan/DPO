from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from UI.GUI.views.View import View
from UI.GUI.views.StartView import StartView
from UI.GUI.views.QuestionView import QuestionView
from UI.GUI.views.SummaryView import SummaryView

from typing import Callable

from form.Question import Question
from form.FormState import FormState

from UI.GUI.Messenger import Messenger

class Window(QWidget):
    def __init__(self, messenger: Messenger):
        super().__init__()
        self.messenger = messenger

        self.setWindowTitle("Fomulár k DPO")
        self.resize(1920, 1080)

        self.stack = QStackedWidget()
        start = StartView()
        self.redirect(start)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)

    def create_question_view(self, question: Question) -> QuestionView:  
        pass

    def new_view(self) -> None:
        q: Question | None = self.messenger.get_question()
        if q is not None:
            view = self.create_question_view(q)
            self.redirect(view)
        else:
            view = SummaryView(self.messenger.form.qna)
            self.redirect(view)
        
        return

    def redirect(self, new: View, msg: str= "") -> None:
        self.stack.addWidget(new)
        self.stack.setCurrentWidget(new)

        if len(msg) != 0:
            new.success(msg)