"""
# Ex 5.03 - QCheckBox PyQt5 Widgets
http://codetorial.net/pyqt5/widget/qcheckbox.html
"""
# https://doc.qt.io/qt-5/qtwidgets-module.html
#  - QPushButton
#  - QLabel
#  - QCheckBox *
#  - QRadioButton
#  - QComboBox
# ...

print(__doc__)

import sys
import _add_syspath_root
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QCheckBox,
                    )
def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex5.03-QCheckBox'
        self.posXY = (300, 300)
        self.windowSize = (400, 200)
        self.initUI()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

    def initUI(self):
        self.cb = QCheckBox('SHOW STATUS ON SCREEN', self)
        self.cb.move(20, 20)
        self.cb.toggle()
        self.cb.stateChanged.connect(self.changeTitle)

        self.show_echo_screen()
        self.show_basic()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('O.K CHECKED!')
        else:
            self.setWindowTitle('')
        self.show_echo_screen()

    def show_echo_screen(self):
        comment = "ON = 2" if self.cb.checkState() else "OFF = 0\n"
        print(f"CHECK STATUS : {comment}")


if __name__ == '__main__':
    main()
