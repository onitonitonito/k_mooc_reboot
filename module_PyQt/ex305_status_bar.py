"""
# Ex 3.05-set status bar
# http://codetorial.net/pyqt5/basics/statusbar.html
"""

import sys
from PyQt5.QtWidgets import (
                        QApplication,
                        QMainWindow,
                    )


print(__doc__)


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'Ex3.05 - set status bar'
        self.posXY = (100, 100)
        self.windowSize = (400, 200)

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()



if __name__ == '__main__':
    main()
