"""
# image read
"""

import cv2
import matplotlib.pyplot as plt

from _path import get_cut_dir

print(__doc__)


dir_home = get_cut_dir('openCV_TAcademy')
img = cv2.imread(dir_home + '/src/dir_home + cat.bmp')

# img type = ndarray
print(type(img))

# check image on window
plt.imshow(img)
plt.show()
