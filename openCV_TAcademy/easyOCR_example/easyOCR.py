"""
# Colab example - news daum : https://bit.ly/2QtrcrD
"""
# TODO: NOT FINISHED YET!

print(__doc__)

import PIL
import easyocr
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from PIL import ImageDraw
from _path import DIR_HOME, get_cut_dir, stop_if_none

dir_ocr = DIR_HOME + 'src\\easyOCR\\'
dir_read = DIR_HOME + 'src\\readOCR\\'
dir_result = DIR_HOME + 'src\\resultOCR\\'


# filename = 'korean.png'                 #  5 recogs
# filename = 'namecard_extracted.png'     #  7 recogs
# filename = 'english.png'                # 11 recogs
# filename = 'news_daum.png'              # 41 recogs
# filename = 'AI_compete_2020_KOGAS.jpg'  # 72 recogs
filename = 'booksOrig090.jpg'            #  recogs

size_targeted = (640, 400)              # resize scale
post_fix = filename.split('.')[0].split('_')[0]

# TO LOAD IMAGE
im = PIL.Image.open(dir_read + filename)
im = stop_if_none(im, message='Image loading failed!')

print('filename =', filename)
print('img size =', im.size, '\n\n')

im_resize = im.resize(size_targeted, PIL.Image.ANTIALIAS)
im_resize = stop_if_none(im_resize, message='Image loading failed!')

# TO SHOW IMAGES : ORIGINAL vs. RESIZE
# im_resize.show()
# im.show()             # NO need ... im_boxed image shows

reader = easyocr.Reader(['en', 'ko',])
bounds = reader.readtext(dir_read + filename)

# Draw bounding boxes
def draw_boxes(image, bounds, color='red', width=3):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image


im_boxed = draw_boxes(im, bounds)
im_boxed.show()


# 저장할 파일 Type : JPEG, PNG 등
# 저장할 때 Quality 수준 : 보통 95 사용
im_boxed.save(dir_result + f"im_boxed_{post_fix}.png", "png", quality=95 )

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
fig, axes = plt.subplots(2,2, figsize=(9,4))
plt.suptitle(f"chart_{post_fix}.png",fontsize=20, y=1.01)     # y=gap

df_probs[1].plot(
                ax=axes[0,0],
                title="probablity plot",
                grid=1,
            )
df_probs[1].plot(
                kind='hist',
                ax=axes[0,1],
                title="histogram & boxplot",
                grid=1,
            )
df_probs[1].plot(
                kind='bar',
                ax=axes[1,0],
                grid=1,
            )
sns.boxplot(
                df_probs[1],
                ax=axes[1,1],
            )

plt.savefig(dir_result + f"chart_{post_fix}.png")
plt.show()
