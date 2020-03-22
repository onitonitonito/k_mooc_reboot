"""
# ex01_04 set Qt Designer.ui link to python file
# https://wikidocs.net/35482
"""
import sys
import _add_syspath_root
from assets import config

from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
                        QApplication,
                        QMainWindow,
                    )

# UI파일 연결 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(config.dir_ui + "01_04_texteditTest.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언 ... MyApp() class MyApp(QWidget) :
class MyApp(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.icon = config.dir_icon + 'icon_qt.png'
        self.title = "1.04 Dialog BOX - First Example"
        self.posXY = (600, 40)
        self.windowSize = (330, 230)

        self.setupUi(self)      # IMPORTANT for form_class!
        self.initUI()
        self.basicShow()

    def initUI(self):
        pass

    def basicShow(self):
        # 프로그램 화면을 보여주는 코드
        self.setWindowIcon(QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()




if __name__ == "__main__" :
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # MyApp의 인스턴스 생성
    window = MyApp()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()


    # app = QApplication(sys.argv)
    # window = MyApp()
    # sys.exit(app.exec_())
