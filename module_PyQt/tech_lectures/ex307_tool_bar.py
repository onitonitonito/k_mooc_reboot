"""
# Ex 3.07 - set tool bar.py
# http://codetorial.net/pyqt5/basics/toolbar.html
"""

import sys; import _add_syspath_root

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

        self.title = 'Ex 3.07-set tool bar'
        self.posXY = (100, 100)
        self.windowSize = (400, 200)
        self.imageName = dir_img +  'img_exit.png'

        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon(self.imageName), 'Exit!', self)
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

        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()



if __name__ == '__main__':
    main()
