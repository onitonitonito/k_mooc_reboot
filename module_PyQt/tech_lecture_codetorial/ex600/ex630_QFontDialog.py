"""
# Ex 6.30_QFontDialog.py
# http://codetorial.net/pyqt5/dialog/qfontdialog.html
"""
## Ex 6-3. QFontDialog.
print(__doc__)

import _add_syspath_root
from assets.config import dir_icon

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QVBoxLayout,
                        QPushButton,
                        QSizePolicy,
                        QLabel,
                        QFontDialog
                    )


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.icon = dir_icon + 'icon_qt.png'
        self.title = 'Ex6.30_QFontDialog'
        self.posXY = (300, 45)
        self.windowSize = (300, 250)

        self.initUI()
        self.showBasic()

    def initUI(self):
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)
        btn.clicked.connect(self.showDialog)

        vbox = QVBoxLayout()
        vbox.addWidget(btn)

        self.lbl = QLabel('The quick brown fox jumps over the lazy dog', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

    def showBasic(self):
        """Basic Attribution & Geometry Display"""
        self.setWindowIcon(QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()


    def showDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
           self.lbl.setFont(font)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
