def base() -> str:
    return """
        QWidget {
            background-color: white;
            color: black;
            font-family: Ubuntu;
            font-size: 20 px;
        }

        QLabel {
            font-size: 30 px;
            font-family: Ubuntu;
        }

        QRadioButton {
            font-size: 20 px;
            font-family: Ubuntu;
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
