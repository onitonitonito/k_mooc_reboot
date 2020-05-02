"""
# Ex 6.40_QFileDialog.py
# http://codetorial.net/pyqt5/dialog/qfiledialog.html
"""
# Ex 6-4. QFileDialog.
print(__doc__)


import _add_syspath_root
from assets.config import dir_icon

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
                        QApplication,
                        QMainWindow,
                        QTextEdit,
                        QAction,
                        QFileDialog,
                    )

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.icon = dir_icon + 'icon_qt.png'
        self.title = 'Ex6.40_QFileDialog'
        self.posXY = (300, 45)
        self.windowSize = (500, 600)

        self.initUI()
        self.showBasic()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)


    def showBasic(self):
        """Basic Attribution & Geometry Display"""
        self.setWindowIcon(QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()


    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
