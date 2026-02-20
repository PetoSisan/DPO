from form.IFormManager import IFormManager
from PySide6.QtWidgets import QApplication

from form.Form import Form

class GUIFormManager(IFormManager):
    def __init__(self, form: Form):
        super().__init__(form)
    
    def run(self):
        pass
        # self.app = QApplication([])
        # self.window = QWidget()
        # self.window.show()
        # self.app.exec()
    

    def quit(self) -> None:
        self.app.quit()