
# import vlc
import webbrowser
import subprocess
import sys
import os

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QFrame, QApplication)
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Connor\'s Template'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Network Connectivity Test
        button = QPushButton('Network Connectivity Test', self)
        button.move(20, 40)
        button.clicked.connect(self.on_click_1)

        # Network Connectivity Test Log
        self.button2 = QPushButton('Open Log', self)
        self.button2.move(300, 40)
        self.button2.clicked.connect(self.on_click_2)

        self.show()

    @pyqtSlot()
    def on_click_1(self):
        os.system("network_connectivity.sh")
        self.button2.setStyleSheet("color: black; background-color: green;")

    def on_click_2(self):
        # open log
        os.system('notepad.exe pass_2019-03-29.log')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
