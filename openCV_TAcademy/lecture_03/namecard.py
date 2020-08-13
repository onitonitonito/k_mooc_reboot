"""
# Tesseract-ocr 설치하기

# 1. tesseract-ocr-w64-setup-v5.0.0-alpha.20191030.exe 파일 다운로드
#    (https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe)
# 2. 설치 시 "Additional script data" 항목에서 "Hangul Script", "Hangul vertical script" 항목 체크,
#    "Additional language data" 항목에서 "Korean" 항목 체크.
# 4. 설치 후 시스템 환경변수 PATH에 Tesseract 설치 폴더 추가
#    (e.g.) c:/Program Files/Tesseract-OCR
# 4. 설치 후 시스템 환경변수에 TESSDATA_PREFIX를 추가하고, 변수 값을 <Tesseract-DIR>/tessdata 로 설정
# 5. <Tesseract-DIR>/tessdata/script/ 폴더에 있는 Hangul.traineddata, Hangul_vert.traineddata 파일을
#    <Tesseract-DIR>/tessdata/ 폴더로 복사
# 6. 명령 프롬프트 창에서 pip install pytesseract 명령 입력
"""

from typing import List

import sys
import cv2
import numpy as np
import pytesseract


from _path import get_cut_dir
dir_src = get_cut_dir('openCV_TAcademy') + '/src/'

def reorderPts(pts: List) -> List:
    """ # re-dorder 4 point of rectangular"""
    idx = np.lexsort((pts[:, 1], pts[:, 0]))  # 칼럼0 -> 칼럼1 순으로 정렬한 인덱스를 반환
    pts = pts[idx]  # x좌표로 정렬

    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]

    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]

    return pts


# 영상 불러오기 : default = namecard1.jpg
# filename = sys.argv[1] if len(sys.argv) > 1 else filename = 'namecard1.jpg'
filename = 'namecard1.jpg'

if len(sys.argv) > 1:
    filename = sys.argv[1]


src_RGB = cv2.imread(dir_src + filename)

# 영상 로딩이 안될경우 시스템 종료!
if src_RGB is None:
    print('Image load failed!')
    sys.exit()

# 출력 영상 설정
dw, dh = 720, 400
src_quards = np.array([[0, 0], [0, 0], [0, 0], [0, 0]], np.float32)        # empty array
destin_quards = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32) # C-Clock wise

dst = np.zeros((dh, dw), np.uint8)

# 입력 영상 전처리
src_gray = cv2.cvtColor(src_RGB, cv2.COLOR_BGR2GRAY)
th, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 바이너리 이미지(src_bin) 에서 외곽선 검출하고 그 중에 명함추출 하는 방법
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    # 너무 작은 객체는 제외 = 면적이 1,000픽셀보다 작은 객체는 제외
    if cv2.contourArea(contour) < 10000:
        continue

    # 외곽선의 근사치 주적 알고리즘 = DP (Douglas-Peucker) algorithm
    #  - Point 수를 줄이는 방식은 Douglas-Peucker algorithm.
    #  - 임의의 폭 안쪽으로 들어오지 않는 포인트를 삭제해 나가면서 외곽선 추출
    approx = cv2.approxPolyDP(contour, cv2.arcLength(contour, True)*0.02, True)

    # 컨벡스가 아니거나 4각형(4 contour)이 아니면 제외 시킴
    if not cv2.isContourConvex(approx) or len(approx) != 4:
        continue

    print(f'*** CHECK: {len(approx)} points found!')

    cv2.polylines(src_RGB, [approx], True, (0, 255, 0), 2, cv2.LINE_AA)
    src_quards = reorderPts(approx.reshape(4, 2).astype(np.float32))

    pers = cv2.getPerspectiveTransform(src_quards, destin_quards)
    dst = cv2.warpPerspective(src_RGB, pers, (dw, dh), flags=cv2.INTER_CUBIC)

    dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    src_RGB_resized = cv2.resize(src=src_RGB, dsize=(0,0), fx=0.4, fy=0.4)


    # print(pytesseract.image_to_string(dst_rgb), lang='Hangul+eng')
    # print(pytesseract.image_to_string(dst_rgb))

    # cv2.imshow('src_RGB', src_RGB)
    cv2.imshow('src_RGB_resized', src_RGB_resized)
    # cv2.imshow('src_gray', src_gray)
    # cv2.imshow('src_bin', src_bin)
    cv2.imshow('destination-extracted namecard', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()
