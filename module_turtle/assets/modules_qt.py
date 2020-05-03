import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QInputDialog,
                        QLineEdit,
                    )

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'QInputDialog'
        self.posxy = (50, 50)
        self.windowSize = (400, 500)

    def initUI(self):
        # self.getChoice()
        # self.getText()
        self.showBasic()

    def getChoice(self):
        items = ("Red","Blue","Green")
        item, okPressed = QInputDialog.getItem(
                                self,
                                "Get item",
                                "Color:",
                                items,
                                0,
                                False,
                            )
        if okPressed and item:
            return item

    def getInteger(self):
        i, okPressed = QInputDialog.getInt(
                                self,
                                "Get integer",
                                "Percentage:",
                                28,
                                0,
                                100,
                                1,
                            )
        if okPressed:
            print(i)

    def getText(self, winTitle, captionHead, initValue=""):
        text, okPressed = QInputDialog.getText(
                                self,
                                winTitle,
                                captionHead,
                                QLineEdit.Normal,
                                initValue,
                            )
        if okPressed and text != '':
            return text

    def getDouble(self):
        d, okPressed = QInputDialog.getDouble(
                                self,
                                "Get double",
                                "Value:",
                                10.05,
                                0,
                                100,
                                10,
                            )
        if okPressed:
            print(d)

    def showBasic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posxy, *self.windowSize)
        self.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)

    ma = MyApp()
    posxy = (0,0)
    windowsize = (300,200)

    while True:
        ma.setGeometry(*posxy, *windowsize)
        _ = ma.getText("Turtle Moves", "Enter angle, move forward :")
        print(f"... {_}")

    sys.exit(app.exec_())
