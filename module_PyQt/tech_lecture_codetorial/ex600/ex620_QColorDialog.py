"""
# Ex 6.20_QColorDialog.py
http://codetorial.net/pyqt5/dialog/qcolordialog.html
"""
# http://doc.qt.io/qt-5/qcolordialog.html

print(__doc__)

import _add_syspath_root
from assets.config import dir_icon

import sys
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QFrame,
                        QPushButton,
                        QColorDialog,
                    )

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.icon = dir_icon + 'icon_qt.png'
        self.title = 'Ex6.20_QColorDialog'
        self.posXY = (300, 45)
        self.windowSize = (300, 250)
        self.initUI()
        self.showBasic()

    def initUI(self):
        col = QColor(232, 109, 197) #rgb(232, 109, 197)


        # SET LABEL DESCRIBE
        lb = QLabel('PICK COLOR FROM PALLETE :', self)
        lb.move(10, 20)

        # SET PUSH BUTTON
        self.btn = QPushButton('Color Pick!', self)
        self.btn.move(110, 210)
        self.btn.clicked.connect(self.showDialog)

        # SET COLOR FRAME
        self.frm = QFrame(self)
        self.frm.setStyleSheet(
                    'QWidget { background-color: %s }'%col.name()
                )
        self.frm.setGeometry(70, 50, 170, 150)

    def showBasic(self):
        """Basic Attribution & Geometry Display"""
        self.setWindowIcon(QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

    def showDialog(self):
        """CallBack() When 'Color Pick!' btn.clicked.connect"""
        col = QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet(
                    'QWidget { background-color: %s }'%col.name()
                )



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
