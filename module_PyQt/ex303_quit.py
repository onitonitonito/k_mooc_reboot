"""
# Ex 3.03-quit button
# http://codetorial.net/pyqt5/basics/closing.html
"""

import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (
                        QWidget,
                        QApplication,
                        QPushButton,
                    )


print(__doc__)


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'Ex3.03 - Quit Button Set'
        self.posXY = (100, 100)
        self.windowSize = (400, 200)

        self.initUI()

    def initUI(self):
        button = QPushButton('Quit', self)
        button.move(50, 50)
        button.resize(button.sizeHint())
        button.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()


if __name__ == '__main__':
    main()
