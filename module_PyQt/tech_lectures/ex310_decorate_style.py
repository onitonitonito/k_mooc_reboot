"""
# Ex 3.10 decorate the style.py
http://codetorial.net/pyqt5/basics/stylesheet.html
"""
print(__doc__)

import sys; import _add_syspath_root

from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QVBoxLayout,
                    )


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex3.10-decarate the stylesheet'
        self.posXY = (300, 300)
        self.windowSize = (400, 300)

        self.initUI()

    def initUI(self):
        lab_red = QLabel('Red')
        lab_green = QLabel('Green')
        lab_blue = QLabel('Blue')

        lab_red.setStyleSheet(
                    "color: red;"
                    "background-color: #F1BDE5;"

                    "border-style: solid;"
                    "border-width: 2px;"
                    "border-color: #FA8072;"
                    "border-radius: 10px;"
                )

        lab_green.setStyleSheet(
                    "color: green;"
                    "background-color: #7FFFD4;"
                )

        lab_blue.setStyleSheet(
                    "color: blue;"
                    "background-color: #87CEFA;"

                    "border-style: dashed;"
                    "border-width: 3px;"
                    "border-color: #1E90FF"
                )

        vBox = QVBoxLayout()
        vBox.addWidget(lab_red)
        vBox.addWidget(lab_green)
        vBox.addWidget(lab_blue)
        self.setLayout(vBox)

        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()





if __name__ == '__main__':
    main()
