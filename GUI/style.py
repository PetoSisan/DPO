def base() -> str:
    return """
        QWidget {
            background-color: white;
            color: black;
            font-family: DejaVu Sans;
            font-size: 12 px;
        }

        QLabel {
            font-size: 16 px;
            font-family: DejaVu Sans;
        }

        QPushButton {
            background-color: #4CAF50;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 6px;
        }

        QPushButton:hover {
            background-color: #45a049;
        }
    """
