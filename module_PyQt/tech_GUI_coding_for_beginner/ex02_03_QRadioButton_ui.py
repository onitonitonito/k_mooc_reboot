"""
# 02.03 QRadinButton_ui
# https://wikidocs.net/35486
"""
# QT디자이너로 uis 폴더에 미리 폼을 제작해서 저장해 둔다

import sys
import _add_syspath_root
from assets.config import dir_icon, dir_ui

from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
                        QMainWindow,
                        QApplication,
                        QRadioButton,
                    )

form_class = uic.loadUiType(dir_ui + "02_03_radiobuttonTest.ui")[0]

class MyApp(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.icon = dir_icon + 'icon_qt.png'

        self.setupUi(self)
        self.initUI()
        self.basicShow()

    def initUI(self):
        #GroupBox안에 있는 RadioButton들을 연결합니다.
        #GroupBox의 자세한 설명은 02.14 GroupBox를 참고하세요.
        self.rbtn1.clicked.connect(self.rbtnFunction)
        self.rbtn2.clicked.connect(self.rbtnFunction)
        self.rbtn3.clicked.connect(self.rbtnFunction)
        self.rbtn4.clicked.connect(self.rbtnFunction)

    def rbtnFunction(self) :
        if self.rbtn1.isChecked()   : print("rbtn1 Chekced")
        elif self.rbtn2.isChecked() : print("rbtn2 Checked")
        elif self.rbtn3.isChecked() : print("rbtn3 Checked")
        elif self.rbtn4.isChecked() : print("rbtn4 Checked")

    def basicShow(self):
        self.setWindowIcon(QIcon(self.icon))
        self.show()




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    Window = MyApp()
    sys.exit(app.exec_())
