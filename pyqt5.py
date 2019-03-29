
# import vlc
# import webbrowser
# import subprocess
import sys
import os

# from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel,
    QFrame, QApplication)
# from PyQt5.QtGui import QColor
# from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Connor\'s Template'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 220
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('SN:')
        self.nameLabel.move(5, 5)
        self.textbox = QLineEdit(self)
        self.textbox.move(40, 0)
        self.textbox.resize(280, 20)

        # Network Connectivity Test
        button = QPushButton('Network Connectivity Test', self)
        button.move(20, 40)
        button.clicked.connect(self.on_click_1)

        # Network Connectivity Test Log
        self.button2 = QPushButton('Open Log', self)
        self.button2.move(300, 40)
        self.button2.clicked.connect(self.on_click_2)

        self.button3 = QPushButton('Do Nothing', self)
        self.button3.move(20, 80)
        self.button3.clicked.connect(self.on_click_3)

        self.button4 = QPushButton('Do Nothing', self)
        self.button4.move(300, 80)
        self.button4.clicked.connect(self.on_click_4)

        self.button5 = QPushButton('Do Nothing', self)
        self.button5.move(20, 120)
        self.button5.clicked.connect(self.on_click_5)

        self.button6 = QPushButton('Do Nothing', self)
        self.button6.move(300, 120)
        self.button6.clicked.connect(self.on_click_6)

        self.button7 = QPushButton('Do Nothing', self)
        self.button7.move(20, 160)
        self.button7.clicked.connect(self.on_click_7)

        self.button8 = QPushButton('Do Nothing', self)
        self.button8.move(300, 160)
        self.button8.clicked.connect(self.on_click_8)



        self.show()

    @pyqtSlot()
    def on_click_1(self):
        os.system("network_connectivity.sh")
        self.button2.setStyleSheet("color: black; background-color: green;")

    def on_click_2(self):
        # open log
        os.system('notepad.exe pass_2019-03-29.log')

    def on_click_3(self):
        print("do nothing")

    def on_click_4(self):
        print("do nothing")

    def on_click_5(self):
        print("do nothing")

    def on_click_6(self):
        print("do nothing")

    def on_click_7(self):
        print("do nothing")

    def on_click_8(self):
        print("do nothing")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
