"""
# Scrollbar on Matplotlib showing page - StackOverFlow.com
# https://stackoverflow.com/
  questions/42622146/scrollbar-on-matplotlib-showing-page
"""
#  - I want to know if there is a manner to put a scrollbar (horz. or vert.)
#  - on a matplotlib showing page (plt.show) that contains several sublots
#  - (sublot2grid). At the moment, the only solution I find is to make the
#  - subplots very small, which isn't very elegant at all.

print(__doc__)

import sys
import random
import matplotlib
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import (
                        QWidget,
                        QApplication,
                        QMainWindow,
                        QVBoxLayout,
                        QScrollArea,
                    )

from matplotlib.backends.backend_qt5agg import (
                        FigureCanvasQTAgg,
                        NavigationToolbar2QT,
                    )

# Make sure that we are using QT5
matplotlib.use('Qt5Agg')

# create a figure and some subplots
FIG, AXES = plt.subplots(ncols=4, nrows=5, figsize=(16,16))

for AX in AXES.flatten():
    random_array = [random.randint(1, 30) for i in range(10)]
    AX.plot(random_array)

def main():
    app = QApplication(sys.argv)
    window = MyApp(FIG)
    sys.exit(app.exec_())

class MyApp(QWidget):
    def __init__(self, fig):
        super().__init__()
        self.title = 'VERTICAL, HORIZONTAL SCROLLABLE WINDOW : HERE!'
        self.posXY = (700, 40)
        self.windowSize = (1200, 800)
        self.fig = fig
        self.initUI()

    def initUI(self):
        QMainWindow().setCentralWidget(QWidget())

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        canvas = FigureCanvasQTAgg(self.fig)
        canvas.draw()

        scroll = QScrollArea(self)
        scroll.setWidget(canvas)

        nav = NavigationToolbar2QT(canvas, self)
        self.layout().addWidget(nav)
        self.layout().addWidget(scroll)

        self.show_basic()

    def show_basic(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()


if __name__ == '__main__':
    main()
