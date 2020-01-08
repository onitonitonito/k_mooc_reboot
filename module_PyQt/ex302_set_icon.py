"""
# Ex 3.02-set icon
# http://codetorial.net/pyqt5/basics/icon.html
"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

from assets.config import dir_icon

print(__doc__)


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'Ex3.02 - set Icon'
        self.posXY = (100, 100)
        self.windowSize = (400, 300)
        self.imageName = dir_icon + 'icon_web.png'

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.setWindowIcon(QIcon(self.imageName))
        self.show()


if __name__ == '__main__':
    main()
