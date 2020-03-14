"""
# Ex 5.08_QSlider_Qdial.py
http://codetorial.net/pyqt5/widget/qprogressbar.html
"""
# https://wikidocs.net/35495
# https://doc.qt.io/qt-5/qslider.html
# ...
#  - QLineEdit
#  - QLineEdit (Advanced)
#  - QProgressBar
#  - QSlider & QDial *
#  - QSplitter
#  - QGroupBox
#  - QTabWidget
#  - QTabWidget (Advanced)
#  - QPixmap
# ...

print(__doc__)

import sys
import _add_syspath_root

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QSlider,
                        QDial,
                        QPushButton,
                    )

def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex5.8_QSlider_Qdial'
        self.posXY = (1200, 50)
        self.windowSize = (370, 250)
        self.initUI()

    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(30, 30)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2)

        self.dial = QDial(self)
        self.dial.move(30, 60)
        self.dial.setRange(0, 50)
        self.dial.setNotchesVisible(True)

        btn = QPushButton('RESET', self)
        btn.move(35, 190)

        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        btn.clicked.connect(self.button_clicked)

        self.show_basic()

    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)


    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()



if __name__ == '__main__':
    main()
