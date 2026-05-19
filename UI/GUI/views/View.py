import os
from pathlib import Path

from typing import Callable

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QMessageBox
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from GUI.style import base

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


    def validate_form(self, line_edits: list[QLineEdit]) -> int:
        empty = 0
        
        for line_edit in line_edits:
            if len(line_edit.text().strip()) == 0:
                line_edit.setStyleSheet("border: 2px solid red;")
                empty += 1
        
        if empty != 0:
            self.error("These required fields are empty.", f"❌ {empty} empty fields")
        
        
        return empty


    # def prepare_table(self, table: QTableWidget, rows: int, columns_names: list[str]) -> None:
    #     table.setRowCount(rows)
    #     table.setColumnCount(len(columns_names))
    #     table.setHorizontalHeaderLabels(columns_names)
    

    # def resize_table(self, table: QTableWidget) -> None:
    #     table.resizeColumnsToContents()
    #     table.resizeRowsToContents()

    #     width = table.verticalHeader().width() + sum([table.columnWidth(i) for i in range(table.columnCount())])
    #     height = table.horizontalHeader().height() + sum([table.rowHeight(i) for i in range(table.rowCount())])

    #     # Set fixed size to match content
    #     table.setFixedSize(width + 10, height + 10)

    
    # def fill_table_row_values(self, table: QTableWidget, row: int, values: list[str], start: int = 0) -> None:
    #     for i, value in enumerate(values):
    #         table.setItem(row, start + i, QTableWidgetItem(value))
    

    # def fill_table_row_buttons(self, table: QTableWidget, row: int, btns: list[QPushButton], start: int) -> None:
    #     for i, btn in enumerate(btns):
    #         table.setCellWidget(row, start + i, btn)


    def align_center(self, parent: QWidget, child: QWidget) -> None:
        layout = QVBoxLayout(parent)
        layout.addWidget(child)
        layout.setAlignment(child, Qt.AlignCenter)



    def error(self, msg: str, title: str = "❌ Error") -> None:
        QMessageBox.warning(self, title, msg)


    def success(self,msg: str, title: str = "✅ Success") -> None:
        QMessageBox.information(self, title, msg)

        