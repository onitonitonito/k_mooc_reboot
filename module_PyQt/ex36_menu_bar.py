"""
# Ex 3.6-set menu bar
# http://codetorial.net/pyqt5/basics/menubar.html
"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
                        QApplication,
                        QMainWindow,
                        QAction,
                        qApp,
                    )

print(__doc__)


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exit_action = QAction(QIcon('img_exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit QApplication')
        exit_action.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exit_action)

        self.setWindowTitle('Ex 3.6-set menu bar')
        self.setGeometry(100, 100, 400, 200)
        self.show()



if __name__ == '__main__':
    main()
