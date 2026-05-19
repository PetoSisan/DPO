from UI.GUI.views.View import View

from typing import Callable

class StartView(View):
    def __init__(self, start: Callable[[], None], quit: Callable[[], None]):
        super().__init__("start.ui")
        self.ui.start.clicked.connect(start)
        self.ui.quit.clicked.connect(quit)