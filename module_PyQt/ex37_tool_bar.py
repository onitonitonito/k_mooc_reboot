"""
# Ex 3.7 - set tool bar.py
# http://codetorial.net/pyqt5/basics/toolbar.html
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
        exitAction = QAction(QIcon('img_exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit QApplication')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        """ Ex3.6 - Same cascaded Exit, But different Menu
        # menuBar = self.menuBar()
        # menuBar.setNativeMenuBar(False)

        # fileMenu = menuBar.addMenu('&File')
        # fileMenu.addAction(exitAction)
        """

        # Ex3.7 - direct 'Exit' toolbar : can be moved anywhere
        self.tooBar = self.addToolBar('Exit')
        self.tooBar.addAction(exitAction)

        self.setWindowTitle('Ex 3.7-set tool bar')
        self.setGeometry(100, 100, 400, 200)
        self.show()



if __name__ == '__main__':
    main()
