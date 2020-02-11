"""
# Ex 4.02 - Lay-out schematic design (box lay-out)
http://codetorial.net/pyqt5/layout/box_layout.html
"""
#  4.01 - 절대적 배치
#  4.02 - 박스 레이아웃 *
#  4.03 - 그리드 레이아웃

print(__doc__)

import sys; import _add_syspath_root
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QPushButton,
                        QHBoxLayout,
                        QVBoxLayout,
                    )


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex4.02-BOX LAY-OUT'
        self.posXY = (300, 300)
        self.windowSize = (400, 200)

        self.MarginRate_H = (1, 1)
        self.MarginRate_V = (8, 1)

        self.initUI()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

    def initUI(self):
        buttonOK = QPushButton('OK')
        buttonCancel = QPushButton('CANCEL')

        hBox = QHBoxLayout()
        hBox.addStretch(3)
        hBox.addWidget(buttonOK)
        hBox.addWidget(buttonCancel)
        hBox.addStretch(1)

        vBox = QVBoxLayout()
        vBox.addStretch(self.MarginRate_V[0])
        vBox.addLayout(hBox)
        vBox.addStretch(self.MarginRate_V[1])

        self.setLayout(vBox)
        self.show_basic()


if __name__ == '__main__':
    main()
