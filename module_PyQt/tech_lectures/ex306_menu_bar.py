"""
# Ex 3.06-set menu bar
# http://codetorial.net/pyqt5/basics/menubar.html
"""

import sys

; import _add_syspath_root

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
                        QApplication,
                        QMainWindow,
                        QAction,
                        qApp,
                    )
from assets.config import dir_img

print(__doc__)


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'Ex 3.06-set menu bar'
        self.imageName = dir_img + 'img_exit.png'
        self.posXY = (100, 100)
        self.windowSize = (400, 200)

        self.initUI()

    def initUI(self):
        exit_action = QAction(QIcon(self.imageName), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit QApplication')
        exit_action.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exit_action)

        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()



if __name__ == '__main__':
    main()
