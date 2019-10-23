"""
# Stack Over Flow - post 1st. answer
# 'numpy.ndarray' object has no attribute 'imshow'
# --------
# http://bit.ly/2VI0FHq
"""
# 스오플에 첫 포스트를 올리다 ... 2019. 5/21
# subplots 는 'numpy.ndarray' 에 plt 오브젝트를 배열
# ax 에 직접 imshow()를 쓸 수 없음.
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt

from skimage import data

'''Read the image data'''
img = data.chelsea()   # cat image


'''Show the image data'''
# Create figure with 1 subplot
fig, axs = plt.subplots(nrows=1, ncols=5, figsize=(10, 3))


print(axs)
# [<matplotlib.axes._subplots.AxesSubplot object at 0x000001D7A841C710>
#  <matplotlib.axes._subplots.AxesSubplot object at 0x000001D7AA58FCC0>
#  <matplotlib.axes._subplots.AxesSubplot object at 0x000001D7AA5C2390>
#  <matplotlib.axes._subplots.AxesSubplot object at 0x000001D7AA5E9A20>
#  <matplotlib.axes._subplots.AxesSubplot object at 0x000001D7AA61A128>]

print(axs.shape)  # (5,)

# Show the image data in a subplot
for i, ax in enumerate(axs):
    print(ax)     # AxesSubplot(0.125,0.11;0.133621x0.77)
    img_made_changeable = img[i:(i + 2) * 50]
    ax.imshow(img_made_changeable, interpolation='none' )

# Show the figure on the screen
plt.show()
