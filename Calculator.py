# Python Calculator using PyQt6

import os
import sys
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.operators = "+-/*%"
        self.setWindowTitle("Calculator By Somil")
        self.display = QLineEdit()
        self.label = QLabel("Note: '%' works as the modulo sign here (remainder).")
        self.setWindowIcon(QIcon(resource_path("Calculator Logo.png")))
        self.InitUI()

    def InitUI(self):
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setMinimumHeight(65)
        self.resize(320,480)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        layout.addWidget(self.display)
        self.display.setReadOnly(True)
        self.display.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        grid = QGridLayout()
        layout.addLayout(grid)
        layout.addWidget(self.label)

        self.label.setStyleSheet("""
            color: grey;
            font-size: 11px;
""")

        self.setStyleSheet("""
            QMainWindow{
                background-color: #1e1e2e;
            }
            QLineEdit{
                background-color: #2a2a3c;
                color: #ffffff;
                font-size: 28px;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                padding: 10px
            }
            QPushButton{
                background-color: #313244;
                color: #ffffff;
                font-size: 18px;
                font-weight: bold;
                border-radius: 8px;
            }
            QPushButton:hover{
                background-color: #45475a;
            }
            QPushButton:pressed{
                background-color: #585b70;
            }
""")

        buttons = [
            ('C', 0, 0), ('%', 0, 1), ('=', 0, 2), ('DEL', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('00', 4, 0), ('0', 4, 1), ('.', 4, 2), ('-', 4, 3),
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            grid.addWidget(button,row,col)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            button.clicked.connect(lambda checked, t=text: self.on_click(t))
        

    def on_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error!")
        elif text == "C":
            self.display.clear()
        elif text == "DEL":
            if self.display.text() == "Error!":
                self.display.clear()
            else: 
                result = self.display.text()
                self.display.setText(result[:-1])
        else:
            if self.display.text() == "Error!":
                self.display.clear()
            if text in self.operators:
                check = self.display.text()
                if check and check[-1] in self.operators:
                    result = self.display.text()
                    self.display.setText(result[:-1])
            current_text = self.display.text()
            self.display.setText(current_text + text)

    def keyPressEvent(self, event):
        key = event.text()
        if key and key in "0123456789+-/*%.":
            self.on_click(key)
        elif event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.on_click('=')
        elif event.key() == (Qt.Key.Key_Backspace):
            self.on_click('DEL')
    

def main():
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()