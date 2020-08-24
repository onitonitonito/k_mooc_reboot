"""
# EASY-OCR : by PyTorch
"""
# !pip install easyocr -> torch build falied!
# [ISSUE] torch build failed! = https://bit.ly/3aSVk9n
# conda install pytorch torchvision cudatoolkit=10.2 -c pytorch

# !npx degit JaidedAI/EasyOCR/examples -f
# npx = execute npm package binaries
# https://www.npmjs.com/package/npx

print(__doc__)

import cv2
import PIL
import easyocr

from PIL import ImageDraw
from _path import (DIR_SRC, get_cut_dir, stop_if_none)

dir_ocr = DIR_SRC + 'easyOCR\\'

# 01 CV2-object
src = cv2.imread(dir_ocr + 'english.png')
src = stop_if_none(src, message='Image loading failed!')

# cv2.imshow('src', src)
# cv2.waitKey()

# show an image
# type = <class 'PIL.PngImagePlugin.PngImageFile'>
# <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=905x480 at..>

# im = PIL.Image.open(dir_ocr + 'english.png')
# im.show()

# Create a reader to do OCR.
reader = easyocr.Reader(['en', 'ko'])
bounds = reader.readtext(dir_ocr + 'english.png')

def draw_boxes(image, bounds, color='yellow', width=2):
    """
    # draw box in image : ROI=Region of Interest
    # Draw bounding boxes
    """
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

draw_boxes(src, bounds)
