"""
# Ex 5.02 - QLabel PyQt5 Widgets
http://codetorial.net/pyqt5/widget/index.html
"""
#  - QPushButton
#  - QLabel *
#  - QCheckBox
#  - QRadioButton
#  - QComboBox
#  - QLineEdit
#  - QLineEdit (Advanced)
#  - QProgressBar
#  - QSlider & QDial
#  - QSplitter
#  - QGroupBox
#  - QTabWidget
#  - QTabWidget (Advanced)
#  - QPixmap
#  - QCalendarWidget
#  - QSpinBox
#  - QDoubleSpinBox
#  - QDateEdit
#  - QTimeEdit
#  - QDateTimeEdit
#  - QTextBrowser
#  - QTextBrowser (Advanced)
#  - QTextEdit

print(__doc__)

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QLabel,
                        QVBoxLayout,
                        QHBoxLayout,
                    )
def main():
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ex5.01-QPushButton'
        self.posXY = (300, 300)
        self.windowSize = (400, 200)
        self.initUI()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

    def initUI(self):
        # DEFINE FONT_01 ATTRIBUTIONS
        font_01 = self.font()
        font_01.setPointSize(20)
        font_01.setBold(True)

        # DEFINE FONT_02 ATTRIBUTIONS
        font_02 = self.font()
        font_02.setFamily('Times New Roman')

        # DEFINE QLABEL
        # VH_CENTER = ADD label_02.setAlignment(Qt.AlignHCenter)
        label_01 = QLabel('First Label', self)
        label_01.setFont(font_01)
        label_01.setAlignment(Qt.AlignCenter)

        label_02 = QLabel('Second Label', self)
        label_02.setFont(font_02)
        label_02.setAlignment(Qt.AlignVCenter)

        # DEFINE BOX LAY-OUT!
        layout = QVBoxLayout()
        layout.addWidget(label_01)
        layout.addWidget(label_02)

        # SET LAY-OUT
        self.setLayout(layout)
        self.show_basic()


if __name__ == '__main__':
    main()
