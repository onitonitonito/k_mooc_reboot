"""
# Ex 5.06 - QLineEdit.py
http://codetorial.net/pyqt5/widget/qlineedit.html
"""
# http://doc.qt.io/qt-5/qlineedit.html
# ...
#  - QLineEdit *
#  - QLineEdit (Advanced)
#  - QProgressBar
#  - QSlider & QDial
#  - QSplitter
#  - QGroupBox
#  - QTabWidget
#  - QTabWidget (Advanced)
#  - QPixmap
# ...

print(__doc__)

import sys
import _add_syspath_root
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QLineEdit,
                    )
def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex5.06-QLineEdit'
        self.posXY = (400, 50)
        self.windowSize = (310, 170)
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

if __name__ == '__main__':
    main()
