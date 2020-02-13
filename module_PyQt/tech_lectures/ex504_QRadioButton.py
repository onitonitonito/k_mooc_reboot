"""
# Ex 5.04 - QRadioButton.py
http://codetorial.net/pyqt5/widget/qradiobutton.html
"""
# https://doc.qt.io/qt-5/qradiobutton.html
#  - QPushButton
#  - QLabel
#  - QCheckBox
#  - QRadioButton *
#  - QComboBox
# ...

print(__doc__)

import sys
import _add_syspath_root
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QRadioButton,
                    )
def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex5.04-QRadioButton'
        self.posXY = (700, 50)
        self.windowSize = (300, 100)
        self.initUI()

    def initUI(self):
        radioBTN1 = QRadioButton('FIRST BUTTON', self)
        radioBTN1.move(50, 30)

        radioBTN2 = QRadioButton(self)
        radioBTN2.move(50, 50)
        radioBTN2.setText('SECOND BUTTON')

        self.show_basic()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

if __name__ == '__main__':
    main()
