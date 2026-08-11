import os
from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMessageBox, QVBoxLayout, QWidget


class View(QWidget):
    def __init__(self, design_file: str, parent: QWidget | None = None):
        super().__init__(parent)
        self.load_ui(design_file)
        self.resize(1920, 1080)

    def load_ui(self, design_file: str):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "design" / design_file)
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close()
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui)

    def error(self, msg: str, title: str = "❌ Error") -> None:
        QMessageBox.warning(self, title, msg)

    def success(self, msg: str, title: str = "✅ Success") -> None:
        QMessageBox.information(self, title, msg)
