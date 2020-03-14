"""
# Ex 5.07_QProgressBar.py
http://codetorial.net/pyqt5/widget/qprogressbar.html
"""
# https://doc.qt.io/qt-5/qprogressbar.html
# ...
#  - QLineEdit
#  - QLineEdit (Advanced)
#  - QProgressBar *
#  - QSlider & QDial
#  - QSplitter
#  - QGroupBox
#  - QTabWidget
#  - QTabWidget (Advanced)
#  - QPixmap
# ...

print(__doc__)

import sys
import _add_syspath_root

from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import (
                        QWidget,
                        QApplication,
                        QPushButton,
                        QProgressBar,
                    )

def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex5.7_QProgressBar'
        self.posXY = (300, 40)
        self.windowSize = (400, 300)
        self.initUI()

    def initUI(self):
        self.pb = QProgressBar(self)
        self.pb.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('START', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.show_basic()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()


    def doAction(self):
        if (self.step < 100 and self.timer.isActive()):
            self.timer.stop()
            self.btn.setText('START')

        elif (self.step >= 100 and self.timer.isActive() != True):
            self.step = 0
            self.pb.setValue(self.step)
            self.btn.setText('START')

        else:
            self.timer.start(100, self)
            self.btn.setText('STOP')


    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('FINISHED!')
            return

        self.step += 1
        self.pb.setValue(self.step)


if __name__ == '__main__':
    main()
