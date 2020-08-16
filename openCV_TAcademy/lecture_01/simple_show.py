"""
# IMAGE READ/SHOW : NO USE OF MATPLOTLIB
# BE CAREFUL OF RGB <-> BGR
"""
# src(RGB) -> cv2(BGR) <-> plt(RGB)

print(__doc__)

import cv2
import matplotlib.pyplot as plt
from _path import (DIR_SRC, get_cut_dir, stop_if_none)

# VARIOUS IMAGE READUNG : cv2 <-> plt
src = cv2.imread(DIR_SRC + 'cat.bmp', cv2.IMREAD_UNCHANGED)
src = stop_if_none(src, message='Image loading failed!')

src2 = plt.imread(DIR_SRC + 'cat.bmp', format='RGB')
src2 = stop_if_none(src2, message='Image loading failed!')

srcRGB = cv2.cvtColor(src2, cv2.COLOR_BGR2RGB)
srcRGB = stop_if_none(srcRGB, message='Image loading failed!')


# img type = ndarray
[print(f"TYPE = {type(obj)}") for obj in [src, src2, srcRGB]]

# cv2 imshow()
cv2.imshow('src', src)
cv2.imshow('src2', src2)

cv2.waitKey()
cv2.destroyAllWindows()

# matplotlib = check image on window
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10,7), )
ax.imshow(src)
plt.show()
