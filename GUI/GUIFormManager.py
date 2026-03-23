from PySide6.QtWidgets import QApplication

from form.Form import Form
from form.IFormManager import IFormManager

from GUI.views.Window import Window

class GUIFormManager(IFormManager):
    def __init__(self, form: Form):
        super().__init__(form)
    
    def run(self):
        self.app = QApplication([])
        self.window = Window()
        self.window.show()
        self.app.exec()
    

    def quit(self) -> None:
        self.app.quit()