"""
# Brunch by JS.Seo - http://bit.ly/2LPnZ65
# --------
# Visual C++ image processing programming image source
# https://raw.githubusercontent.com/gilbutITbook
#       /006796/master/images/ch07/camera7.bmp
"""

# 이미지 프로세싱 플랜 나누기 연습(3)
# gray scale 1 byte = 8 bit .... 11111111 = 255
# --------
#   - 1픽셀 BW값는 0 or 1 이다 ... 바이너리 픽셀
#   - 1픽셀 Gray값는 0 ~ 255 (1byte=8bit)이다 ... 0b1111_1111 = 255
#   - 8 비트 그레이 스케일의 각 자릿수를, BW값 바이너리 픽셀 8장으로 분해
#   - 최하위 비트는  값이 너무 작아서 그림 상에 영향을 거의 미치지 않지만,
#     원하는 숨은 그림을 새겨 넣을 수 있다 (워터마크와 유사).
# img data references = skimage.data.camera()
print(__doc__)

''' now fixing & refactoring '''
import cv2
import matplotlib.pyplot as plt
from skimage import data

# imshow needs 2d,3d ndarray format
img_camera = data.camera()
img_camera7 = cv2.imread('camera7.bmp', cv2.IMREAD_GRAYSCALE)
img_watermark7 = cv2.imread('number7.bmp', cv2.IMREAD_GRAYSCALE)


def main():
    """
    (1) bit slicing comparison : Watermark vs. Non-Watermark
    (2) Sample B/W image cannot be divided multiple bit plane = just 2.
    """
    # ''' 두 방법의 차이를 결과로 비교해 본다.'''
    # compare draw_img_old vs. draw_img
    # ax = fig.add_subplot vs. fig, axs = plt.subplots()

    slice_bit_plan(img_camera)
    slice_bit_plan(img_camera7)
    slice_bit_plan(img_watermark7)


def draw_img_old(original, bit_imgs, title, sub_title):
    """ drawing original & divided 8 imgs. """
    fig = plt.figure(figsize=(17, 7))
    fig.suptitle(title)

    for i in range(1,10):
        if i == 1:
            ax = fig.add_subplot(2, 5, i)
            ax.imshow(original, cmap='gray')
            ax.set_title(sub_title)

        elif i < 6:
            ax = fig.add_subplot(2, 5, 12-i)
            ax.imshow(bit_imgs[i-2], cmap='gray')
            ax.set_title(f"BIT [{i-2}]")

        else:
            ax = fig.add_subplot(2, 5, 11-i)
            ax.imshow(bit_imgs[i-2], cmap='gray')
            ax.set_title(f"BIT [{i-2}]")
    plt.show()


def draw_img(original, bit_imgs, title, sub_title):
    """ drawing original & divided 8 imgs. """
    fig, axs = plt.subplots(nrows=2, ncols=5, figsize=(17, 7))
    fig.suptitle(title)
    print(axs.shape)        # (2,5)

    img_number = 8

    for i, ax in enumerate(axs):
        for j, a in enumerate(ax):
            img_number -= 1

            if i == 0  and j == 0:
                a.imshow(original, cmap='gray')
                a.set_title(sub_title)
                img_number += 1
                print(i,j,'original')

            elif i == 1 and j == 0:
                img_number += 1
                print(i,j,'-- pass --')

            else:
                a.imshow(bit_imgs[img_number], cmap='gray')
                a.set_title(f"BIT [{img_number}]")
                print(i,j, img_number)

        print(ax.shape)
        print(i, ax)
    plt.show()


def slice_bit_plan(img):
    bit_imgs = [img.copy() for i in range(8)]
    row, col = img.shape

    for i in range(row):
        for j in range(col):
            for k in range(8):
                bit_imgs[k][i, j] = 255 if img[i, j] & [1 << k] else 0

    # remain the last bit plan ... watermark
    cv2.imwrite("bit8_slicing_last.bmp", bit_imgs[0])

    draw_img(img, bit_imgs, "Bit Plane Slicing", "ORIGINAL")


if __name__ == '__main__':
    main()
