"""
# cv2 window view : 
"""

import sys
import cv2
from _path import get_cut_dir

# 영상 불러오기
dir_home = get_cut_dir('openCV_TAcademy')
img = cv2.imread(dir_home + '/src/cat.bmp')

if img is None:
    print('Image load failed!')
    sys.exit()

# 영상 화면 출력
cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey()

# 창 닫기
cv2.destroyAllWindows()
