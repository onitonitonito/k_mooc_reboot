"""
# Ex 3.8 set Window to the center of screen
# http://codetorial.net/pyqt5/basics/centering.html
"""

import sys

from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QDesktopWidget,
                    )

print(__doc__)


def main():
    app = QApplication(sys.argv)

    win_false = MyApp(False)    # placed a bit up position!
    win_true = MyApp(True)      # move a bit down ... real center!

    sys.exit(app.exec_())


class MyApp(QWidget):
    def __init__(self, flag):
        super().__init__()
        self.flag = flag
        self.initUI()

    def initUI(self):
        self.setWindowTitle(f'Ex 3.8-center /w (flag={self.flag})')
        self.resize(700, 500)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        print(f"qr = {qr}")  # PyQt5.QtCore.QRect(0, 0, 400, 300)

        cp = QDesktopWidget().availableGeometry().center()
        print(f"cp = {cp}")  # PyQt5.QtCore.QPoint(959, 514)
        print()

        # MOVE 'QtRect' to move 'CENTER POINT'
        qr.moveCenter(cp)

        if self.flag:
            # DOWN to MENU-STRIP HEIGHT
            self.move(qr.topLeft())



if __name__ == '__main__':
    main()
