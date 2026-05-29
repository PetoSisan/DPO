from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from UI.GUI.views.View import View
from UI.GUI.views.StartView import StartView
from UI.GUI.views.QuestionView import QuestionView
from UI.GUI.views.SummaryView import SummaryView
from UI.GUI.views.SingleChoiceQuestionView import SingleChoiceQuestionView
from UI.GUI.views.MultipleChoiceQuestionView import MultipleChoiceQuestionView

from typing import Callable

from form.Question import Question
from form.FormState import FormState

from UI.GUI.Messenger import Messenger

from form.SingleChoiceQuestion import SingleChoiceQuestion
from form.MultipleChoiceQuestion import MultipleChoiceQuestion

from UI.GUI.Messenger import Messenger

class Window(QWidget):
    def __init__(self, messenger: Messenger, project_id: str):
        super().__init__()
        self.messenger = messenger

        self.setWindowTitle("Fomulár k DPO")
        self.resize(1920, 1080)

        self.stack = QStackedWidget()
        start = StartView(project_id, self.new_view, messenger.quit)
        self.redirect(start)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)
    

    def create_question_view(self, question: Question) -> QuestionView:  
        if isinstance(question, SingleChoiceQuestion):
            return SingleChoiceQuestionView(question, self.messenger.add_answers)
        
        return MultipleChoiceQuestionView(question, self.messenger.add_answers)

    def new_view(self) -> None:
        q: Question | None = self.messenger.get_question()
        if q is not None:
            view = self.create_question_view(q)            
        else:
            view = SummaryView(self.messenger.summary(), self.messenger.quit)

        self.redirect(view)
        return

    def redirect(self, new: View, msg: str= "") -> None:
        self.stack.addWidget(new)
        self.stack.setCurrentWidget(new)

        if len(msg) != 0:
            new.success(msg)