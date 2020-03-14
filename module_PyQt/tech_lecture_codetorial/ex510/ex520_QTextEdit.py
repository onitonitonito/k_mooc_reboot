"""
# Ex 5.20_QTextEdit.py
http://codetorial.net/pyqt5/widget/qdatetimeedit.html
"""
# ...
#  - QCalendarWidget
#  - QSpinBox
#  - QDoubleSpinBox
#  - QDateEdit
#  - QTimeEdit
#  - QDateTimeEdit
#  - QTextBrowser
#  - QTextBrowser (Advanced)
#  - QTextEdit *

print(__doc__)

import _add_syspath_root
from assets.config import dir_icon

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QTextEdit,
                        QVBoxLayout,
                    )

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.icon = dir_icon + 'icon_qt.png'
        self.title = 'Ex5.20_QTextEdit'
        self.posXY = (600, 45)
        self.windowSize = (300, 300)
        self.initUI()
        self.showBasic()

    def initUI(self):
        self.lbl1 = QLabel('Enter your sentence:')
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        self.lbl2 = QLabel('The number of words is 0')

        self.te.textChanged.connect(self.text_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

    def showBasic(self):
        """Basci Attribution & Geometry display"""
        self.setWindowIcon(QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

    def text_changed(self):
        text = self.te.toPlainText()
        self.lbl2.setText('The number of words is ' + str(len(text.split())))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
