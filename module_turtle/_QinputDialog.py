"""
# PyQT5 input dialog - Python Tutorial
# https://pythonspot.com/pyqt5-input-dialog/
"""
print(__doc__)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 input dialogs - pythonspot.com'
        self.posXY = (1300, 700)
        self.winSize = (640, 480)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.winSize)

        self.getInteger("Get integer", "Percentage:")
        self.getDouble("Get double", "Value:")
        self.getChoice("Get item", "Color:")
        self.getText("Get text", "Your name:")

        self.show()

    def getInteger(self, winTitle, caption):
        i, okPressed = QInputDialog.getInt(self, winTitle, caption, 28, 0, 100, 1)
        if okPressed: print(i)

    def getDouble(self, winTitle, caption):
        d, okPressed = QInputDialog.getDouble(self, winTitle, caption, 10.50, 0, 100, 10)
        if okPressed: print( d)

    def getChoice(self, winTitle, caption):
        items = ("Red","Blue","Green")
        item, okPressed = QInputDialog.getItem(self, winTitle, caption, items, 0, False)
        if okPressed and item: print(item)

    def getText(self, winTitle, caption):
        text, okPressed = QInputDialog.getText(self, winTitle, caption, QLineEdit.Normal, "")
        if okPressed and text != '': print(text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ma = MyApp()
    sys.exit(app.exec_())
