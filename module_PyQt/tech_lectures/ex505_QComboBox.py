"""
# Ex 5.04 - QRadioButton.py
http://codetorial.net/pyqt5/widget/qradiobutton.html
"""
# http://doc.qt.io/qt-5/qcombobox.html
#  - QPushButton
#  - QLabel
#  - QCheckBox
#  - QRadioButton
#  - QComboBox *
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
        self.posXY = (1200, 50)
        self.windowSize = (300, 170)
        self.initUI()

    def initUI(self):
        # w/o claiming an instance
        QRadioButton('FIRST BUTTON', self).move(50, 30)

        # w/ claiming an instance
        rb1 = QRadioButton('SECOND BUTTON', self).move(50, 60)

        # stack function on an instance
        rb2 = QRadioButton('THIRD BUTTON', self)
        rb2.move(50, 90)

        # stack over & over
        rb3 = QRadioButton(self)
        rb3.move(50, 120)
        rb3.setText('FOURTH BUTTON')

        self.show_basic()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

if __name__ == '__main__':
    main()
