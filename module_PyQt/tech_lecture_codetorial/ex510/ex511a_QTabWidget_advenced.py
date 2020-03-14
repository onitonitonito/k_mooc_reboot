"""
# Ex 5.11a_QTabWidget_advenced.py
http://codetorial.net/pyqt5/widget/qtabwidget_advanced.html
"""
# ...
#  - QLineEdit
#  - QLineEdit (Advanced)
#  - QProgressBar
#  - QSlider & QDial
#  - QSplitter
#  - QGroupBox
#  - QTabWidget
#  - QTabWidget (Advanced) *
#  - QPixmap
# ...

print(__doc__)

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class MyApp(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Ex5.11a_QTabWidget_advenced'
        self.posXY = (500, 50)
        self.windowSize = (350, 300)
        self.initUI()

    def initUI(self):
        tabs = QTabWidget()
        tabs.addTab(FirstTab(), 'First')
        tabs.addTab(SecondTab(), 'Second')
        tabs.addTab(ThirdTab(), 'Third')

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addWidget(buttonbox)

        self.setLayout(vbox)

        self.show_basic()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

class FirstTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        name = QLabel('Name:')
        nameedit = QLineEdit()

        age = QLabel('Age:')
        ageedit = QLineEdit()

        nation = QLabel('Nation:')
        nationedit = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(name)
        vbox.addWidget(nameedit)
        vbox.addWidget(age)
        vbox.addWidget(ageedit)
        vbox.addWidget(nation)
        vbox.addWidget(nationedit)
        vbox.addStretch()

        self.setLayout(vbox)

class SecondTab(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lan_group = QGroupBox('Select Your Language')
        combo = QComboBox()
        list = ['Korean', 'English', 'Chinese']
        combo.addItems(list)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(combo)
        lan_group.setLayout(vbox1)

        learn_group = QGroupBox('Select What You Want To Learn')
        korean = QCheckBox('Korean')
        english = QCheckBox('English')
        chinese = QCheckBox('Chinese')

        vbox2 = QVBoxLayout()
        vbox2.addWidget(korean)
        vbox2.addWidget(english)
        vbox2.addWidget(chinese)
        learn_group.setLayout(vbox2)

        vbox = QVBoxLayout()
        vbox.addWidget(lan_group)
        vbox.addWidget(learn_group)
        self.setLayout(vbox)

class ThirdTab(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel('Terms and Conditions')
        text_browser = QTextBrowser()
        text_browser.setText('This is the terms and conditions')
        checkbox = QCheckBox('Check the terms and conditions.')

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(text_browser)
        vbox.addWidget(checkbox)

        self.setLayout(vbox)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
