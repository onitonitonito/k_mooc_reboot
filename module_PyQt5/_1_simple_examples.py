#!/usr/bin/python3
""" ZetCode PyQt5 tutorial

    Author: Jan Bodnar
    Website: zetcode.com
    Last edited: August 2017
"""
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMessageBox

class Example(QWidget):
    """ In this example, we create a simple window in PyQt5.
    """
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):

        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class ExampleMessageBox(Example):
    """ This program shows a confirmation
 message box when we click on the close
 button of the application window. """
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main_simple_window():   # class Example()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

def main_message_box():     # class ExampleMessageBox()
    app = QApplication(sys.argv)
    ex01 = ExampleMessageBox()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # main_simple_window()
    main_message_box()
