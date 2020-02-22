"""
# Ex 5.09_QSlider_Qdial.py
http://codetorial.net/pyqt5/widget/qsplitter.html
"""
# https://wikidocs.net/35495
# https://doc.qt.io/qt-5/qslider.html
# ...
#  - QLineEdit
#  - QLineEdit (Advanced)
#  - QProgressBar
#  - QSlider & QDial
#  - QSplitter *
#  - QGroupBox
#  - QTabWidget
#  - QTabWidget (Advanced)
#  - QPixmap
# ...

print(__doc__)

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QHBoxLayout,
                        QFrame,
                        QSplitter,
                    )

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex5.10_QSlider_Qdial'
        self.posXY = (1200, 50)
        self.windowSize = (500, 500)
        self.initUI()

    def initUI(self):
        # SET 4 FRAMES
        top = QFrame()
        top.setFrameShape(QFrame.Box)

        midleft = QFrame()
        midleft.setFrameShape(QFrame.StyledPanel)

        midright = QFrame()
        midright.setFrameShape(QFrame.Panel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Sunken)

        # SET HORIZONTAL SPLITTER
        sp1 = QSplitter(Qt.Horizontal)
        sp1.addWidget(midleft)
        sp1.addWidget(midright)

        # SET VERTICAL SPLITTER
        sp2 = QSplitter(Qt.Vertical)
        sp2.addWidget(top)
        sp2.addWidget(sp1)
        sp2.addWidget(bottom)

        # SET SPLITTER INTO HBOX LAY-OUT
        hbox = QHBoxLayout()
        hbox.addWidget(sp2)

        # SET LAY-OUT
        self.setLayout(hbox)
        self.show_basic()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
