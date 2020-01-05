"""
# Scrollbar on Matplotlib showing page - StackOverFlow.com
# https://stackoverflow.com/questions/42622146/scrollbar-on-matplotlib-showing-page
"""
#  - I want to know if there is a manner to put a scrollbar (horz. or vert.)
#  - on a matplotlib showing page (plt.show) that contains several sublots
#  - (sublot2grid). At the moment, the only solution I find is to make the
#  - subplots very small, which isn't very elegant at all.

print(__doc__)

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

# Make sure that we are using QT5
matplotlib.use('Qt5Agg')

from PyQt5 import QtWidgets


class ScrollableWindow(QtWidgets.QMainWindow):
    def __init__(self, fig):
        self.qapp = QtWidgets.QApplication([])

        QtWidgets.QMainWindow.__init__(self)
        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(QtWidgets.QVBoxLayout())
        self.widget.layout().setContentsMargins(0,0,0,0)
        self.widget.layout().setSpacing(0)

        self.fig = fig
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        self.scroll = QtWidgets.QScrollArea(self.widget)
        self.scroll.setWidget(self.canvas)

        self.nav = NavigationToolbar(self.canvas, self.widget)
        self.widget.layout().addWidget(self.nav)
        self.widget.layout().addWidget(self.scroll)

        self.show()
        exit(self.qapp.exec_())


if __name__ == '__main__':
    import random
    # create a figure and some subplots

    fig, axes = plt.subplots(ncols=4, nrows=5, figsize=(16,16))
    for ax in axes.flatten():
        rand_array = [random.randint(1,random.randint(100, 100)) for x in range(10)]
        random.shuffle(rand_array)
        ax.plot(rand_array)

    a = ScrollableWindow(fig)
