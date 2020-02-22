"""
# Ex 5.14_QPixMap.py
http://codetorial.net/pyqt5/widget/qpixmap.html
"""
# ...
#  - QLineEdit
#  - QLineEdit (Advanced)
#  - QProgressBar
#  - QSlider & QDial
#  - QSplitter
#  - QGroupBox
#  - QTabWidget
#  - QTabWidget (Advanced)
#  - QPixmap *
# ...

print(__doc__)

import sys
import _add_syspath_root

from assets.config import dir_img
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QVBoxLayout,
                    )

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex5.14_QPixMap - Free Landscape image'
        self.posXY = (5, 45)
        self.windowSize = (640, 480)
        self.initUI()

    def initUI(self):
        pixmap = QPixmap(dir_img + 'landscape.jpg')
        pixmap_size = (pixmap.width(), pixmap.height())

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)

        explain = "[ Image Size: {} x {} ]".format(
                                            pixmap_size[0],
                                            pixmap_size[1],
                                        )
        describe = QLabel(explain)
        describe.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        vbox.addWidget(describe)
        self.setLayout(vbox)

        self.show_basic()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
