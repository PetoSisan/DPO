from UI.GUI.views.View import View

class SummaryView(View):
    def __init__(self, qna: dict[str, list[str]]):
        super().__init__("summary.ui")
        self.qna = qna