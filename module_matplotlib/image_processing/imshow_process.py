"""
# software carpentry - how to use imshow()
# https://statkclee.github.io/trilobite/skimage-numpy.html
# --------
# imshow() needs numpy array nparray
#
\n\n"""
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from skimage import data

scales = ['gray', 'magma', 'jet']

# imshow needs 2d,3d ndarray
img_coins = data.coins()
img_coffee = data.coffee()
img_cat = data.chelsea()
img_original = data.camera()

img_face_area = img_original[50:180, 160:290] # [y,x]
img_random = np.random.random([300,300])
img_circle = (lambda x, y: np.exp(-(x**2 + y**2) / 15)
              )(*np.ogrid[-5:5:0.1, -5:5:0.1])

def draw_imgs(img, scales=['gray'], figsize=(10, 5)):
    """show 2 bisect imgs - jet / gray scale """

    fig, axs = plt.subplots(ncols=len(scales), nrows=1, figsize=figsize)

    if len(scales) > 1:
        for i, scale in enumerate(scales):
            axs[i].imshow(img, cmap=scale)
            axs[i].set_title(scale.upper())
    else:
        axs.imshow(img, cmap=scales[0])
        axs.set_title(scales[0].upper())

    plt.show()

def main():
    draw_imgs(img_random)
    draw_imgs(img_coffee)
    draw_imgs(img_cat)
    draw_imgs(img_original, scales=scales, figsize=(17, 5))
    draw_imgs(img_face_area, scales=scales, figsize=(10, 5))
    draw_imgs(img_circle, scales=scales, figsize=(10, 5))
    draw_imgs(img_coins, scales=scales, figsize=(17, 5))



if __name__ == '__main__':
    main()
