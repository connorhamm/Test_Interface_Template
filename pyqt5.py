

"""
Logic:
1. Mimic Davros
- set icon size
- set icon position
2. Add push buttons in correct position
3. Add button opening file functionality
4. Add Serial # Input Selection
5. Add Accept and reset button
6. Add in button to merge two photos together
7. 

"""
# import vlc
import webbrowser
import subprocess
import sys
import os

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = ''
        self.left = 10
        self.top = 10
        self.width = 281
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Brilliant Button
        button = QPushButton('Brilliant', self)
        button.move(0, 70)
        button.clicked.connect(self.on_click_1)

        self.show()

    @pyqtSlot()
    def on_click_1(self):
        webbrowser.open_new("https://www.brilliant.org")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
