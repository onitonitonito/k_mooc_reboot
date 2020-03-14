"""
# Ex 5.18_QDateTimeEdit.py
http://codetorial.net/pyqt5/widget/qdatetimeedit.html
"""
# https://doc.qt.io/qt-5/qdatetimeedit.html
# ...
#  - QCalendarWidget
#  - QSpinBox
#  - QDoubleSpinBox
#  - QDateEdit
#  - QTimeEdit
#  - QDateTimeEdit *
#  - QTextBrowser
#  - QTextBrowser (Advanced)
#  - QTextEdit

print(__doc__)

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QDateTimeEdit,
                        QVBoxLayout,
                    )

import _add_syspath_root
from assets.config import dir_icon


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.icon = dir_icon + 'icon_qt.png'
        self.title = 'Ex5.18_QDateTimeEdit'
        self.posXY = (600, 45)
        self.windowSize = (300, 100)
        self.initUI()
        self.showBasic()

    def initUI(self):
        lb = QLabel('QTimeEdit :')

        dte = QDateTimeEdit(self)
        dte.setDateTime(QDateTime.currentDateTime())
        dte.setDateTimeRange(
                    QDateTime(1900, 1, 1, 00, 00, 00),
                    QDateTime(2100, 1, 1, 00, 00, 00),
                )
        dte.setDisplayFormat('yyyy.MM.dd hh:mm:ss')

        vbox = QVBoxLayout()
        vbox.addWidget(lb)
        vbox.addWidget(dte)
        vbox.addStretch()

        self.setLayout(vbox)


    def showBasic(self):
        self.setWindowIcon(QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
