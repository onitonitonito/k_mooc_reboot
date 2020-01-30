"""
# Ex 3.4-show tooltip help
# http://codetorial.net/pyqt5/basics/tooltip.html
"""

import sys

from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QPushButton,
                        QToolTip,
                    )


print(__doc__)


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SanSerif', 10))
        self.setToolTip('This is a <b>Qwidget</b> widget')

        button = QPushButton('Button', self)
        button.setToolTip('This is a <b>Qwidget</b> widget')
        button.move(50, 50)
        button.resize(button.sizeHint())


        self.setWindowTitle('Ex3.4 - show tooltip help')
        self.setGeometry(100, 100, 400, 200)
        self.show()


if __name__ == '__main__':
    main()
