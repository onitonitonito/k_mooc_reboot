"""
# Qtpy Line input turtle
"""
print(__doc__)

import sys
import random
import turtle

from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QLineEdit,
                    )


t = turtle.Turtle()
t.home()
t.speed(0)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex5.06-QLineEdit'
        self.posXY = (1300, 50)
        self.windowSize = (400, 200)
        self.initUI()

    def initUI(self):
        self.lab = QLabel(self)
        self.lab.move(60, 40)

        qle = QLineEdit(self)
        qle.move(60, 100)
        qle.textChanged[str].connect(self.onChanged)

        self.show_basic()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

    def onChanged(self, text):
        self.lab.setText(text)
        self.lab.adjustSize()
        t.setheading(random.randint(0,360))
        self.main()

    def main(self):
        for i in range(6):
            t.left(56)
            t.forward(50)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.main()
    turtle.mainloop()
    sys.exit(app.exec_())
