"""
# Ex 3.2-set icon
# http://codetorial.net/pyqt5/basics/icon.html
"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

print(__doc__)


def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Ex3.2 - set Icon')
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon('img_web.png'))
        self.show()


if __name__ == '__main__':
    main()
