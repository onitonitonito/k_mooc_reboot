"""
# PyQt5 test - main / sub window event test
"""
#     - main = pop push button window
#     - sub  = pop progressbar window
#     - sub  = pop explorer w/ dir_target.

print(__doc__)

import sys
import openpyxl
import ctypes
import subprocess

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon

user32 = ctypes.windll.user32
screen_width, screen_height = (user32.GetSystemMetrics(i) for i in range(2))

(window_width, window_height) = 450, 150

# DIR_TARGET = 'C:/'
DIR_TARGET = "C:/Users"

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton("push!", self)
        self.btn.clicked.connect(self.btn_clicked)

        self.setWindowTitle('Excel Pixel_mainWindow')
        # self.setWindowIcon(QIcon('icon.png'))
        self.move(screen_width / 2 - window_width / 2,
                  screen_height / 2 - window_height / 2)
        self.resize(window_width, window_height)
        self.show()

    def btn_clicked(self):
        self.subwindiw = SubWindow()


class SubWindow(QWidget):
    def __init__(self):
        super(SubWindow, self).__init__()
        self.th = Thread()
        self.th.start()
        self.initUI()

    def closeEvent(self, QCloseEvent):
        print("test")

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.th.send_value.connect(self.pbar.setValue)

        self.setWindowTitle('Excel Pixel_subWindow')
        # self.setWindowIcon(QIcon('icon.png'))
        self.move(screen_width / 2 - window_width / 2 + 10,
                  screen_height / 2 - window_height / 2 + 10)
        self.resize(window_width, window_height)
        self.show()


class Thread(QThread):
    send_value = pyqtSignal(float)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        for n in range(1, 101):
            print(n)
            self.send_value.emit(n)

            self.msleep(50)

        # 두번 째 창 닫기를 추가할 위치
        # explorer /select, "C:\Users"
        dir_str = ""r'explorer /select, "%s"'"" % ("\\".join(DIR_TARGET.split("/")))
        print(dir_str)
        subprocess.Popen(dir_str)



if __name__ == '__main__':
    main()
