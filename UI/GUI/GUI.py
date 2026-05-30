from PySide6.QtWidgets import QApplication

from form.Form import Form
from UI.UI import UI
from UI.GUI.views.Window import Window

from UI.GUI.Messenger import Messenger


class GUI(UI):
    def __init__(self):
        return

    def run(self, form: Form, project_id: str):
        messenger = Messenger(form, self.quit)

        self.app = QApplication([])
        window = Window(messenger, project_id)
        messenger.register_callback(window.new_view)

        window.show()
        self.app.exec()

    def quit(self) -> None:
        self.app.quit()
