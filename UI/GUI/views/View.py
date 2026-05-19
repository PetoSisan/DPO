import os
from pathlib import Path

from typing import Callable

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QMessageBox
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from UI.GUI.style import base

from form.Question import Question

class View(QWidget):
    def __init__(self, design_file: str, parent: QWidget | None = None):
        super().__init__(parent)
        self.load_ui(design_file)
        self.error_label = None
        self.resize(1920, 1080)


    def load_ui(self, design_file: str):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "design" /  design_file)
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close()
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui)
        

    def error(self, msg: str, title: str = "❌ Error") -> None:
        QMessageBox.warning(self, title, msg)


    def success(self,msg: str, title: str = "✅ Success") -> None:
        QMessageBox.information(self, title, msg)

        