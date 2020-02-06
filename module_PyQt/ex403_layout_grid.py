"""
# Ex 4.03 - Grid Lay-out schematic design
http://codetorial.net/pyqt5/layout/grid_layout.html
"""
#  4.01 - 절대적 배치
#  4.02 - 박스 레이아웃
#  4.03 - 그리드 레이아웃 *

print(__doc__)

import sys
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QGridLayout,
                        QLabel,
                        QLineEdit,
                        QTextEdit,
                    )
def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex4.03-GRID LAY-OUT'
        self.posXY = (300, 300)
        self.windowSize = (400, 200)
        self.initUI()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # PUT LABELS on GRID(Y,X)
        grid.addWidget(QLabel('Title :'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        # PUT INPUT EDIT on GRID(Y,X)
        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)

        # TEXT EDIT GIVES MULTI-LINE EDITOR
        grid.addWidget(QTextEdit(), 2, 1)

        self.show_basic()


if __name__ == '__main__':
    main()
