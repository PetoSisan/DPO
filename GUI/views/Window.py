from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from View import View

from GUI.GUIFormManager import GUIFormManager



# class MainWindow(QWidget):
#     def __init__(self, formMananger: GUIFormManager):
#         super().__init__()
#         self.setWindowTitle("Fomulár k DPO")
#         self.resize(1920, 1080)

#         self.formManager = formMananger
#         self.stack = QStackedWidget()
        
        
#         # self.stack.addWidget(self.sign_in_view)
#         # self.stack.addWidget(self.sign_up_view)

#         self.connect()

#         # self.stack.setCurrentWidget(self.sign_in_view)

#         layout = QVBoxLayout(self)
#         layout.addWidget(self.stack)


#     def connect(self) -> None:
#         # self.sign_in_view.switch_to_sign_up.connect(lambda: self.stack.setCurrentWidget(self.sign_up_view))
#         # self.sign_up_view.switch_to_sign_in.connect(lambda: self.stack.setCurrentWidget(self.sign_in_view))
#         # self.sign_in_view.sign_in.connect(self.sign_in)
#         # self.sign_up_view.sign_up.connect(self.sign_up)
#         pass
    


#     def redirect(self, old: View | None, new: View, msg: str= "") -> None:   
#         if old is not None:
#             self.stack.removeWidget(old)

#         self.stack.addWidget(new)
#         self.stack.setCurrentWidget(new)

#         if len(msg) != 0:
#             new.success(msg)


class Window(QWidget):
    def __init__(self, formMananger: GUIFormManager):
        self.formManager = formMananger
        self.stack = QStackedWidget()
        
        
        # self.stack.addWidget(self.sign_in_view)
        # self.stack.addWidget(self.sign_up_view)


        # self.stack.setCurrentWidget(self.sign_in_view)

        # layout = QVBoxLayout(self)
        # layout.addWidget(self.stack)


    def connect(self) -> None:
        # self.sign_in_view.switch_to_sign_up.connect(lambda: self.stack.setCurrentWidget(self.sign_up_view))
        # self.sign_up_view.switch_to_sign_in.connect(lambda: self.stack.setCurrentWidget(self.sign_in_view))
        # self.sign_in_view.sign_in.connect(self.sign_in)
        # self.sign_up_view.sign_up.connect(self.sign_up)
        pass
    


    def redirect(self, old: View | None, new: View, msg: str= "") -> None:   
        if old is not None:
            self.stack.removeWidget(old)

        self.stack.addWidget(new)
        self.stack.setCurrentWidget(new)

        if len(msg) != 0:
            new.success(msg)