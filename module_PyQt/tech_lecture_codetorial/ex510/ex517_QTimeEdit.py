"""
# Ex 5.17 QTimeEdit.py - SpinBox to Edit Time
http://codetorial.net/pyqt5/widget/qtimeedit.html
"""
# https://doc.qt.io/qt-5/qtimeedit.html
# ...
#  - QCalendarWidget
#  - QSpinBox
#  - QDoubleSpinBox
#  - QDateEdit
#  - QTimeEdit *
#  - QDateTimeEdit
#  - QTextBrowser
#  - QTextBrowser (Advanced)
#  - QTextEdit

print(__doc__)

import sys

from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QTimeEdit,
                        QVBoxLayout,
                    )

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex5.17 QTimeEdit :'
        self.posXY = (600, 45)
        self.windowSize = (300, 100)
        self.initUI()

    def initUI(self):
        lb = QLabel('QTimeEdit')

        te = QTimeEdit(self)
        te.setTime(QTime.currentTime())
        te.setTimeRange(QTime(3, 00, 00), QTime(23, 30, 00))
        te.setDisplayFormat('hh:mm:ss')

        vbox = QVBoxLayout()
        vbox.addWidget(lb)
        vbox.addWidget(te)
        vbox.addStretch()

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
