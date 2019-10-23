"""
# partial image array of chelsea(cat) in axes
# imshow() needs image array of value 0~255
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage import data

'''Read the image data'''
img = data.chelsea()   # cat image

'''Show the image data'''
# Create figure with 1 subplot [1,5]
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
    ax.imshow(img_made_changeable, interpolation='none')

# Show the figure on the screen
plt.show()
