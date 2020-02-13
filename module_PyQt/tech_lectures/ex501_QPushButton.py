"""
# Ex 5.01 - PyQt5 Widgets
http://codetorial.net/pyqt5/widget/index.html
"""
# https://doc.qt.io/qt-5/qradiobutton.html
#  - QPushButton *
#  - QLabel
#  - QCheckBox
#  - QRadioButton
#  - QComboBox
# ...

print(__doc__)

import sys
import _add_syspath_root
from PyQt5.QtWidgets import (
                        QApplication,
                        QWidget,
                        QPushButton,
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

    def set_hBox(self, margin_left, contents, margin_right):
        hBox = QHBoxLayout()
        hBox.addStretch(margin_left)

        for content in contents:
            hBox.addWidget(content)

        hBox.addStretch(margin_right)
        return hBox

    def set_vBox(self, margin_up, contents, margin_down):
        vBox = QVBoxLayout()
        vBox.addStretch(margin_up)

        for content in contents:
            vBox.addLayout(content)

        vBox.addStretch(margin_down)
        return vBox

    def set_layout_HVbox(self, widgets):
        hBoxes = []
        for widget in widgets:
            hBox = self.set_hBox(1, [widget,], 1)
            hBoxes.append(hBox)

        vBox = self.set_vBox(1, hBoxes, 5)
        self.setLayout(vBox)

    def initUI(self):
        # DEFINE WIDGETS
        button_01 = QPushButton('&Button01', self)
        button_01.setCheckable(True)
        button_01.toggle()

        button_02 = QPushButton(self)
        button_02.setText('Button&02')

        button_03 = QPushButton('Button03', self)
        button_03.setEnabled(False)

        vertical_layouts = [button_01, button_02, button_03]
        self.set_layout_HVbox(vertical_layouts)
        self.show_basic()


if __name__ == '__main__':
    main()
