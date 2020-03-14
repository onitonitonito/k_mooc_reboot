"""
# Ex 5.13_QCalendarWidget.py
http://codetorial.net/pyqt5/widget/qpixmap.html
"""
# https://doc.qt.io/qt-5/qcalendarwidget.html
# ...
#  - QCalendarWidget *
#  - QSpinBox
#  - QDoubleSpinBox
#  - QDateEdit
#  - QTimeEdit
#  - QDateTimeEdit
#  - QTextBrowser
#  - QTextBrowser (Advanced)
#  - QTextEdit

print(__doc__)

import sys

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QVBoxLayout,
                        QCalendarWidget,
                    )

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex5.13_QCalendarWidget'
        self.posXY = (600, 45)
        self.windowSize = (430, 300)
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.show_date)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)
        self.show_basic()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

    def show_date(self, date):
        self.lbl.setText(date.toString())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
