"""
# Ex 5.11_QTabWidget.py
http://codetorial.net/pyqt5/widget/qtabwidget.html
"""
# ...
#  - QLineEdit
#  - QLineEdit (Advanced)
#  - QProgressBar
#  - QSlider & QDial
#  - QSplitter
#  - QGroupBox
#  - QTabWidget *
#  - QTabWidget (Advanced)
#  - QPixmap
# ...

print(__doc__)

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,QTabWidget,
                        QVBoxLayout,
                    )

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex5.11_QTabWidget'
        self.posXY = (500, 50)
        self.windowSize = (500, 400)
        self.initUI()

    def initUI(self):
        tab1 = QWidget()
        tab2 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, 'Tab1')
        tabs.addTab(tab2, 'Tab2')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.show_basic()


    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
