"""
# Plotting the data with scrollable x (time/horizontal) axis on Linux
# https://stackoverflow.com/questions/
# 31001713/plotting-the-data-with-scrollable-x-time-horizontal-axis-on-linux
"""
# 슬라이드바를 밀면, 그래프의 좌표값이 변하는 위젯

print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

t = np.arange(0.0, 100.0, 0.01)
s = np.sin(2*np.pi*t)
plt.plot(t,s)
plt.axis([0, 10, -1, 1])

axpos = plt.axes([0.2, 0.1, 0.65, 0.03])
spos = Slider(axpos, 'Pos', 0.1, 90.0)

def update(val):
    pos = spos.val
    ax.axis([pos,pos+10,-1,1])
    fig.canvas.draw_idle()

spos.on_changed(update)
plt.show()
