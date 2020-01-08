"""
# Ex 3.01-pop up window
# http://codetorial.net/pyqt5/basics/opening.html
"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

print(__doc__)


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())


class MyApp(QWidget):
    """
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ex3.01- My First Application')
        self.move(100, 100)       # based on POS_XY [NW]
        self.resize(400, 300)
        self.show()


if __name__ == '__main__':
    main()
