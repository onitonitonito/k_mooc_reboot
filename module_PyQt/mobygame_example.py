"""
# 파이썬으로 만드는 나만의 GUI 프로그램 - Wikidocs
# http://codetorial.net/pyqt5/basics/opening.html
"""
import sys
import ctypes

from assets import script_run
from assets.config import dir_img

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QVBoxLayout,
                    )

print(__doc__)

user = ctypes.windll.user32
screenSize = tuple(user.GetSystemMetrics(i) for i in range(2))

windowSize = (640, 400)
posXY = ((screenSize[0]-windowSize[0])*0.5, (screenSize[1]-windowSize[1])*0.5)

print(f"* SCREEN SIZE = ({screenSize[0]} x {screenSize[1]})", flush=True)
print(f"* WINDOW SIZE = ({windowSize[0]} x {windowSize[1]})", flush=True)
print(f"* START posXY = ({int(posXY[0])}, {int(posXY[1])})", flush=True)


def main():
    app = QApplication(sys.argv)
    window = MyApp(posXY, windowSize)
    sys.exit(app.exec_())

class MyApp(QWidget):
    def __init__(self, posXY, windowSize):
        super().__init__()
        self.title = 'My First PyQt5 Application : HERE!'
        self.windowSize = windowSize
        self.posXY = posXY
        self.initUI()

    def initUI(self):
        # 라벨요소 추가
        logo = QLabel()
        logo.setPixmap(QPixmap(dir_img + 'logo_mobygames.png'))
        logo.setAlignment(Qt.AlignCenter)

        description = QLabel('중앙으로 배치되는 Description Text 입니다.')
        description.setAlignment(Qt.AlignCenter)

        # 메인 V레이아웃에 모든 요소 추가
        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(logo)
        layout.addWidget(description)
        # layout.addSpacing(30)
        layout.addStretch(1)
        self.setLayout(layout)

        self.show_basic()

    def show_basic(self):
        """기본셋팅 - 타이틀, 아이콘, 지오메트리"""
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(dir_img + 'icon_qt.png'))
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()


if __name__ == '__main__':
    main()
