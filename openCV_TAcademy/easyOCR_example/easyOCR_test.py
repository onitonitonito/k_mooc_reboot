"""
# Colab example - news daum : https://bit.ly/2QtrcrD
"""
# TODO: NOT FINISHED YET!

print(__doc__)

import PIL
import easyocr
import pandas as pd
import matplotlib.pyplot as plt

from PIL import ImageDraw
from _path import DIR_SRC, stop_if_none

# imagefile_dir = DIR_SRC + 'easyOCR\\' + 'namecard_extracted.png'  #  7 recogs
# imagefile_dir = DIR_SRC + 'easyOCR\\' + 'news_daum.png'           # 41 recogs
imagefile_dir = DIR_SRC + 'easyOCR\\' + 'AI_compete_2020_KOGAS.jpg' # 72 recogs

# imagefile_dir = DIR_SRC + 'korean.jpg'      # 5 recogs
# imagefile_dir = DIR_SRC + 'english.jpg'     # 11 recogs

# TO LOAD IMAGE
im = PIL.Image.open(imagefile_dir)
im = stop_if_none(im, message='Image loading failed!')

im_resize = im.resize((640, 480), PIL.Image.ANTIALIAS)
im_resize = stop_if_none(im_resize, message='Image loading failed!')

# TO SHOW IMAGES : ORIGINAL vs. RESIZE
# im_resize.show()
im.show()

reader = easyocr.Reader(['en', 'ko',])
bounds = reader.readtext(imagefile_dir)

# Draw bounding boxes
def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image


im_boxed = draw_boxes(im, bounds)
im_boxed.show()


# 저장할 파일 Type : JPEG, PNG 등
# 저장할 때 Quality 수준 : 보통 95 사용
im_boxed.save(dir_ocr + 'im_boxed', "JPEG", quality=95 )


probs, recogs = [], []

for idx, line in enumerate(bounds):
    recognition = line[-2]
    probablity = line[-1] * 100

    recogs.append([idx, recognition])
    probs.append([idx, probablity])

    print(f"{probablity:0.2f} % ... | {recognition:30}")



# TO ANALYZE STATICS of PROBABLITY
df_probs = pd.DataFrame(probs)
print(df_probs[1].describe())

for prob in probs:
    print(prob)

# TO DRAW GRAPH : PLOT / HISTOGRAM
fig, axes = plt.subplots(1,2, figsize=(12,4))
df_probs[1].plot(grid=1, ax=axes[0])
df_probs[1].hist(bins=27, ax=axes[1])
plt.show()
