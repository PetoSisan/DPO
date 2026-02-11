from ..form.Form import IForm
from PySide6.QtWidgets import QApplication

class GUIForm(IForm):
    def __init__(self, qna):
        super().__init__(qna)
    
    def run(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.window.show()
        self.app.exec()
    

    def quit(self) -> None:
        retcode = self.call_callback()
        self.app.exit(retcode)
        return