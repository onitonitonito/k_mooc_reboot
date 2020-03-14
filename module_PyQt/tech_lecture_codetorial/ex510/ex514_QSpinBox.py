"""
# Ex 5.14_QSpinBox.py
http://codetorial.net/pyqt5/widget/qspinbox.html
"""
# https://doc.qt.io/qt-5/qspinbox.html
# ...
#  - QCalendarWidget
#  - QSpinBox *
#  - QDoubleSpinBox
#  - QDateEdit
#  - QTimeEdit
#  - QDateTimeEdit
#  - QTextBrowser
#  - QTextBrowser (Advanced)
#  - QTextEdit

print(__doc__)

import sys

from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QSpinBox,
                        QVBoxLayout,
                    )

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex5.14_QSpinBox'
        self.posXY = (600, 45)
        self.windowSize = (430, 300)
        self.initUI()

    def initUI(self):
        self.lb1 = QLabel('QSpinBox :')

        self.spb = QSpinBox()
        self.spb.setMinimum(-10)
        self.spb.setMaximum(30)
        self.spb.setRange(-10, 30)
        self.spb.setSingleStep(2)
        self.spb.valueChanged.connect(self.value_changed)

        self.lb2 = QLabel('0')

        vbox = QVBoxLayout()
        vbox.addWidget(self.lb1)
        vbox.addWidget(self.spb)
        vbox.addWidget(self.lb2)
        vbox.addStretch()

        self.setLayout(vbox)
        self.show_basic()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

    def value_changed(self):
        self.lb2.setText(str(self.spb.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
