"""
# Ex 3.04-show tooltip help
# http://codetorial.net/pyqt5/basics/tooltip.html
"""

import sys; import _add_syspath_root

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

        self.title = 'Ex3.04 - show tooltip help'
        self.posXY = (100, 100)
        self.windowSize = (400, 200)

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SanSerif', 10))
        self.setToolTip('This is a <b>Qwidget</b> widget')

        button = QPushButton('Button', self)
        button.setToolTip('This is a <b>Qwidget</b> widget')
        button.move(50, 50)
        button.resize(button.sizeHint())

        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()


if __name__ == '__main__':
    main()
