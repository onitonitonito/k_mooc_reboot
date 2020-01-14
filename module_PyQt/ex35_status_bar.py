"""
# Ex 3.5-set status bar
# http://codetorial.net/pyqt5/basics/statusbar.html
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


print(__doc__)


def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setWindowTitle('Ex3.5 - set status bar')
        self.setGeometry(100, 100, 400, 200)
        self.show()



if __name__ == '__main__':
    main()
