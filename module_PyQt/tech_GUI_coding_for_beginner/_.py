import sys
import _add_syspath_root
from assets import config

from PyQt5 import uic
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QMainWindow,
                    )


from_class = uic.loadUiType(uifile=config.dir_ui + 'texteditTest.ui')[0]

class MyApp(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setUI()
        self.basicShow()

    def setUI(self):
        pass

    def basicShow(self):
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    app.exec_()
