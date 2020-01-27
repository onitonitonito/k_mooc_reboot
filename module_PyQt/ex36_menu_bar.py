"""
# Ex 3.6-set menu bar
# http://codetorial.net/pyqt5/basics/menubar.html
"""

import sys
from PyQt5.QtWidgets import (QApplication,
                            QMainWindow,


print(__doc__)


def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.statusBar().showMessage('Ready')

        self.setWindowTitle('Ex 3.6-set menu bar')
        self.setGeometry(100, 100, 400, 200)
        self.show()



if __name__ == '__main__':
    main()
