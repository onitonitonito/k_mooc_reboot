"""
#
#
"""
import sys
import ctypes

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QMainWindow,
                        QStackedWidget,
                        QVBoxLayout,
                    )

from assets.config import dir_img

print(__doc__)

user32 = ctypes.windll.user32
screen_width, screen_height = (user32.GetSystemMetrics(i) for i in range(2))

def main():
    app = QApplication([])
    window = MyApp()
    sys.exit(app.exec_())


class MainWidget(QWidget):
    def __init__(self, window, title, left, top, width, height):
        """
        # left : int, required    - 좌측 여백
        # top : int, required     - 상단 여백
        # width : int, required   - 폭
        # height : int, required  - 높이
        """
        super().__init__()
        self.window = window
        self.setWindowTitle(title)
        self.setGeometry(left, top, width, height)

        # 이동할수 있는 허용범위를 셋팅
        self.move(screen_width / 2 - width / 2,
                  screen_height / 2 - height / 2)

        # 메인 레이아웃
        mainLayout = QVBoxLayout()

        # 로고 이미지, 설명 문구
        logo = QLabel()
        logo.setPixmap(QPixmap(dir_img + 'logo_mobygames.png'))
        logo.setAlignment(Qt.AlignCenter)

        description = QLabel('중앙으로 배치되는 Description Text 입니다.')
        description.setAlignment(Qt.AlignCenter)

        # 메인 레이아웃에 모든 요소 추가
        mainLayout.addWidget(logo)
        mainLayout.addWidget(description)
        mainLayout.addSpacing(30)

        self.setLayout(mainLayout)
        self.setFixedSize(width, height)

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'SET! Window Title Here!'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        self.mainWidget = MainWidget(
            self,
            self.title,
            self.left,
            self.top,
            self.width,
            self.height,
        )

        self.mainWidget.show()

    def showMainWidget(self):
        self.centralWidget.setCurrentWidget(self.mainWidget)


if __name__ == '__main__':
    main()
