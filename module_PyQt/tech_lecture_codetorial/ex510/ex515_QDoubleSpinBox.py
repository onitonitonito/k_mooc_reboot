"""
# Ex 5.15_QDoubleSpinBox.py - Deal real_number floating Point
http://codetorial.net/pyqt5/widget/qdoublespinbox.html
"""
# https://doc.qt.io/qt-5/qdoublespinbox.html
# ...
#  - QCalendarWidget
#  - QSpinBox
#  - QDoubleSpinBox *
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
                        QDoubleSpinBox,
                        QVBoxLayout,
                    )

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex5.15_QDoubleSpinBox'
        self.posXY = (600, 45)
        self.windowSize = (430, 300)
        self.initUI()

    def initUI(self):
        self.lb1 = QLabel('QDoubleSpinBox :')

        self.dspb = QDoubleSpinBox()
        self.dspb.setRange(0, 100)
        self.dspb.setSingleStep(0.5)
        self.dspb.setPrefix('$ ')
        self.dspb.setDecimals(2)
        self.dspb.valueChanged.connect(self.value_changed)

        self.lb2 = QLabel('$ 0.00')

        vbox = QVBoxLayout()
        vbox.addWidget(self.lb1)
        vbox.addWidget(self.dspb)
        vbox.addWidget(self.lb2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.show_basic()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

    def value_changed(self):
        self.lb2.setText(f'$ {self.dspb.value():.2f}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
