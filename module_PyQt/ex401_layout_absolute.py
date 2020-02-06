"""
# Ex 4.01 - Lay-out schematic design (abs.positioning)
http://codetorial.net/pyqt5/layout/absolute_positioning.html
"""
#  4.01 - 절대적 배치 *
#  4.02 - 박스 레이아웃
#  4.03 - 그리드 레이아웃

print(__doc__)

import sys

from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QPushButton,
                    )


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex4.01-Lay-out schematic design'
        self.posXY = (300, 300)
        self.windowSize = (400, 200)

        self.initUI()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

    def initUI(self):
        label01 = QLabel('Lable-01', self).move(30,20)
        label02 = QLabel('Lable-02', self).move(30,60)
        button01 = QPushButton('button-01', self).move(100, 13)
        button02 = QPushButton('button-02', self).move(100, 53)

        self.show_basic()






if __name__ == '__main__':
    main()
