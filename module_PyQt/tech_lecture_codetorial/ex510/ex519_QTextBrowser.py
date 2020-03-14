"""
# Ex 5.19_QTextBrowser.py
http://codetorial.net/pyqt5/widget/qdatetimeedit.html
"""
# ...
#  - QCalendarWidget
#  - QSpinBox
#  - QDoubleSpinBox
#  - QDateEdit
#  - QTimeEdit
#  - QDateTimeEdit
#  - QTextBrowser *
#  - QTextBrowser (Advanced)
#  - QTextEdit

print(__doc__)

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QLineEdit,
                        QTextBrowser,
                        QPushButton,
                        QVBoxLayout,
                    )

import _add_syspath_root
from assets.config import dir_icon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.icon = dir_icon + 'icon_qt.png'
        self.title = 'Ex5.19_QTextBrowser'
        self.posXY = (600, 45)
        self.windowSize = (300, 300)
        self.initUI()
        self.showBasic()

    def initUI(self):
        lb1 = QLabel('TEXT HISTORY :')
        lb2 = QLabel('TYPE & ENTER to Store ABOVE!')

        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text)

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        clear_btn = QPushButton('Clear')
        clear_btn.pressed.connect(self.clear_text)

        vbox = QVBoxLayout()
        vbox.addWidget(lb1)
        vbox.addWidget(self.tb, 1)
        vbox.addWidget(lb2)
        vbox.addWidget(self.le, 0)
        vbox.addWidget(clear_btn, 2)

        self.setLayout(vbox)

    def showBasic(self):
        """Basci Attribution & Geometry display"""
        self.setWindowIcon(QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

    def append_text(self):
        """CallBack() When le.returnPressed.connect"""
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()

    def clear_text(self):
        """CallBack() When clear_btn.pressed.connect"""
        self.tb.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
