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

    def getChoice(self, winTitle, captionHead, items):
        """
        # items = ("Red","Blue","Green")
        """
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

    def getInteger(
            self, winTitle, captionHead, initValue=28,
            start=0, end=100, step=1
        ):
        integer, okPressed = QInputDialog.getInt(
                                self,
                                winTitle,
                                captionHead,
                                initValue,
                                start,
                                end,
                                step,
                            )
        if okPressed:
            return integer

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
    posxy = (400, 700)
    windowsize = (500, 500)

    # winTitle = "Integer"
    # captionHead = "INPUT VALUE :"
    winTitle="TEXT!"
    captionHead="ANGLE, MOVE :"

    def main():
        while True:
            ma.setGeometry(*posxy, *windowsize)
            _value = get_text(winTitle, captionHead)
            print(f"value ... {_value}")

    def get_int(winTitle, captionHead):
        return ma.getInteger(winTitle, captionHead)

    def get_text(winTitle, captionHead):
        return ma.getText(winTitle, captionHead)

    app = QApplication(sys.argv)
    ma = MyApp()
    main()
    sys.exit(app.exec_())
