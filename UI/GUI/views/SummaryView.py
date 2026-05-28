from UI.GUI.views.View import View

from typing import Callable
from form.FormState import FormState

class SummaryView(View):
    def __init__(self, qna: dict[str, list[str]], quit: Callable[[FormState], None]):
        super().__init__("summary.ui")
        self.qna = qna
        self.ui.quit.clicked.connect(lambda: quit(FormState.ABORTED))
        self.ui.submit.clicked.connect(lambda: quit(FormState.DONE))
        self.load_summary()

    def format_summary(self) -> str:
        result = ""

        for question, answers in self.qna.items():
            result += f"<p><b>{question}</b><br>"
            result += "<br>".join(answers)
            
        result += "</p>"
        return result
    

    def load_summary(self) -> None:
        summary = self.format_summary()
        self.ui.summary.setHtml(summary)
