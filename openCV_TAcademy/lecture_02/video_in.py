"""
# simple saved video input test : '/src/vtest.avi'
"""

import sys
import cv2

from _path import get_cut_dir

dir_home = get_cut_dir('openCV_TAcademy')


# 동영상 파일로부터 cv2.VideoCapture 객체 생성
cap = cv2.VideoCapture(dir_home + '/src/avi/input.avi')
video_on = cap.isOpened()

if not video_on:
    print("Camera open failed!")
    sys.exit()

# 프레임 크기
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)


# 프레임 해상도, 전체 프레임수, FPS 출력
print('Frame width:', width)
print('Frame height:', height)
print('Frame count:', count)
print('FPS:', fps)

delay = round(1000 / fps)

# 매 프레임 처리 및 화면 출력
while video_on:
    ret, frame = cap.read()

    if not ret:
        break

    edge = cv2.Canny(frame, 50, 150)

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)

    if cv2.waitKey(delay) == 27:
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
