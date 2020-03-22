"""
# 02.04 QCheckBox ... to OVERRIDE to 1.04 ui.
# https://wikidocs.net/35488
"""
# QT 디자이너로 작성된 1.04 ui를 쓰면서 타이틀만 오버라이드 시킴!

import sys
import _add_syspath_root
from assets import config

from PyQt5 import uic
from PyQt5.QtGui import QIcon

# 추가적인 import 필요없음? ... Qwidget, QPushButton, QVLayout etc.
from PyQt5.QtWidgets import (QApplication, QMainWindow)

print(__doc__)

# UI파일 연결 ... 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
# ui 화일은 XML 형식으로 Qwidget, QPushButton 등 필요 class 가 명시되어 있음.
# 따라서 클래스 모듈을 따로 불러올 필요없음 = 자동적으로 LOAD 됨
form_class = uic.loadUiType(config.dir_ui + "01_04_texteditTest.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언
class MyApp(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.icon = config.dir_icon + 'icon_qt.png'
        self.title = 'Ex2.4 QcheckBox Test'           # OVERRIDE! to 1.04

        # 디자이너 작성 ui 셋업
        self.setupUi(self)

        # 기본적 ui 셋팅
        self.initUI()

        # 화면에 보여주는 메서드
        self.basicShow()

    def initUI(self):
        """# 버튼에 기능을 연결하는 코드"""
        # GroupBox밖에 있는 CheckBox에 기능 연결
        self.cbx1.stateChanged.connect(self.checkFunction)
        self.cbx2.stateChanged.connect(self.checkFunction)
        self.cbx3.stateChanged.connect(self.checkFunction)
        self.cbx4.stateChanged.connect(self.checkFunction)

        # GroupBox안에 있는 CheckBox에 기능 연결
        self.gcbx1.stateChanged.connect(self.groupCheckFunction)
        self.gcbx2.stateChanged.connect(self.groupCheckFunction)
        self.gcbx3.stateChanged.connect(self.groupCheckFunction)
        self.gcbx4.stateChanged.connect(self.groupCheckFunction)

        # PushButton to clear all CheckBox
        self.pb.clicked.connect(self.pushButtonFunction)

    def checkFunction(self) :
        #CheckBox는 여러개가 선택될 수 있기 때문에 elif를 사용하지 않습니다.
        if self.cbx1.isChecked() : print("Check BOX 1 is Checked!")
        if self.cbx2.isChecked() : print("Check BOX 2 is Checked!")
        if self.cbx3.isChecked() : print("Check BOX 3 is Checked!")
        if self.cbx4.isChecked() : print("Check BOX 4 is Checked!")
        print()

    def groupCheckFunction(self) :
        if self.gcbx1.isChecked() : print("Group Check Box 1 is Checked!")
        if self.gcbx2.isChecked() : print("Group Check Box 2 is Checked!")
        if self.gcbx3.isChecked() : print("Group Check Box 3 is Checked!")
        if self.gcbx4.isChecked() : print("Group Check Box 4 is Checked!")
        print()

    def pushButtonFunction(self):
        if self.cbx1.checkState() :
            print("Clear check box1")


    def basicShow(self):
        """# 기본적인 프로그램 화면을 보여주는 코드"""
        self.setWindowIcon(QIcon(self.icon))
        self.setWindowTitle(self.title)             # OVERRIDE! to 1.04
        self.show()




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    Window = MyApp()
    sys.exit(app.exec_())
