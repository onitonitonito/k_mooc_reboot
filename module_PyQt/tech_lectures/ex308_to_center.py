"""
# Ex 3.08 set Window to the center of screen
# http://codetorial.net/pyqt5/basics/centering.html
"""

import sys; import _add_syspath_root

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
        self.title = f'Ex 3.08-center /w (flag={self.flag})'
        self.windowSize = (400, 300)

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(*self.windowSize)
        self.center()
        self.show()

    def center(self):
        # PyQt5.QtCore.QRect(0, 0, 400, 300)
        qr = self.frameGeometry()
        print(f"qr = {qr}")

        # PyQt5.QtCore.QPoint(959, 514)
        cp = QDesktopWidget().availableGeometry().center()
        print(f"cp = {cp}")

        # MOVE 'QtRect' to move 'CENTER POINT'
        qr.moveCenter(cp)

        # MOVE DOWN as much as MENU-STRIP HEIGHT
        if self.flag:
            self.move(qr.topLeft())



if __name__ == '__main__':
    main()
