from PySide6.QtWidgets import QApplication

from form.Form import Form
from UI.UI import IUI
from UI.GUI.views.Window import Window

class GUI(IUI):
    def __init__(self, form: Form):
        super.__init__(form)
        return


    def run(self):
        self.app = QApplication([])
        self.window = Window(self.form.get_current_question, self.form.add_answers, self.quit)
        self.window.show()
        self.app.exec()
    

    def quit(self) -> None:
        self.app.quit()