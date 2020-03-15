"""
# Ex 6.01_QInputDialog.py
http://codetorial.net/pyqt5/dialog/qinputdialog.html
"""

print(__doc__)

import _add_syspath_root
from assets.config import dir_icon

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QPushButton,
                        QLineEdit,
                        QInputDialog,
                    )

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.icon = dir_icon + 'icon_qt.png'
        self.title = 'Ex6.01_QInputDialog'
        self.posXY = (600, 45)
        self.windowSize = (400, 300)
        self.initUI()
        self.showBasic()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(120, 35)

    def showBasic(self):
        """Basci Attribution & Geometry display"""
        self.setWindowIcon(QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
