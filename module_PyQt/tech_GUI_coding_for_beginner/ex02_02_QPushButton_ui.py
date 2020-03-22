"""
# 02.02 QpushButton_ui
# https://wikidocs.net/35485
"""
# QT디자이너로 uis 폴더에 미리 폼을 제작해서 저장해 둔다

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
form_class = uic.loadUiType(config.dir_ui + "02_02_QPushButtonTest.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언
class MyApp(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.icon = config.dir_icon + 'icon_qt.png'

        # 디자이너 작성 ui 셋업
        self.setupUi(self)

        # 기본적 ui 셋팅
        self.initUI()

        # 화면에 보여주는 메서드
        self.basicShow()

    def initUI(self):
        """# 버튼에 기능을 연결하는 코드"""
        self.btn1.clicked.connect(self.button1Function)
        self.btn2.clicked.connect(self.button2Function)

    def button1Function(self) :
        """# btn1이 눌리면 작동 할 콜백 함수"""
        print("btn1 Clicked!")

    def button2Function(self) :
        """# btn2가 눌리면 작동 할 콜백 함수"""
        print("btn2 Clicked!")

    def basicShow(self):
        """# 기본적인 프로그램 화면을 보여주는 코드"""
        self.setWindowIcon(QIcon(self.icon))
        self.show()




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    Window = MyApp()
    sys.exit(app.exec_())
