"""
# 파이썬으로 만드는 나만의 GUI 프로그램 - Wikidocs
# http://codetorial.net/pyqt5/basics/opening.html
"""
import sys
import ctypes

from assets import script_run
from assets.config import dir_img
from assets.config import dir_statics

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QApplication

print(__doc__)

user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)
win_width = 640
win_height = 480
start_xy = ((screen_width-win_width)*0.5, (screen_height-win_height)*0.5)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 기본셋팅 - 타이틀, 아이콘, 지오메트리
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon(dir_statics + 'icons\\icon_qt.png'))
        self.setGeometry(*start_xy, win_width, win_height)
        # -- all the same above --
        # self.move(start_xy)
        # self.resize(win_width, win_height)

        # 라벨요소 추가
        logo = QLabel()
        logo.setPixmap(QPixmap(dir_img + 'logo_mobygames.png'))
        logo.setAlignment(Qt.AlignCenter)

        description = QLabel('중앙으로 배치되는 Description Text 입니다.')
        description.setAlignment(Qt.AlignCenter)

        # 메인 레이아웃에 모든 요소 추가
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(logo)
        mainLayout.addWidget(description)
        mainLayout.addSpacing(30)

        # 최종 SET & SHOW()
        self.setLayout(mainLayout)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
