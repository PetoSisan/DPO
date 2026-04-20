from PySide6.QtWidgets import QApplication

from form.Form import Form

from GUI.views.Window import Window

class GUI():
    def __init__(self):
        return
    
    def wanted(self) -> bool:
        """Checks whether user wants to fill the form.
        Params:
        
        Returns:
            `True`, if yes, `False` otherwise
        """

        answer: str = input("Prajete si vypĺňať 'Vyjadrenie' k žiadosti DPO? [ano/nie] \n")
        return True if answer.lower() == "ano" else False


    def run(self, form: Form):
        self.app = QApplication([])
        self.window = Window(form.get_current_question, form.add_answers)
        self.window.show()
        self.app.exec()
    

    def quit(self) -> None:
        self.app.quit()