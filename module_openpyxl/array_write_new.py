"""
# 엑셀작업 줄이기 - 엑셀없이 코드로 수정/정리/추출/쓰기
# 보안 잠금된 화일은 안됨 = 읽기/쓰기(코딩) = 조회(엑셀)
#  - 새로운 엑셀형식 화일만들기
"""
# script run 에서는 실행이 안됨 = 이것은 '케바케'
# print(__doc__)

import random
import assets.script_run

from pyprnt import prnt
from assets.configs import dir_home_statics
from assets.classes import write_excel


filename_with_dir = dir_home_statics + "_write.xlsx"

# 자료만들기 4행5열 데이터
title = ['NAME', 'KOR', 'ENG', 'MATH', 'REMARK', ]
names = ['PARK', 'LEE', 'KIM', 'CHOI', 'LIM', 'YU', 'CHEONG', 'SEO']

rows = []
for name in names:
    scores = [random.randrange(40, 100, 5) for i in range(3)]
    rows.append([name, *scores, '-', ])

# 만들어진 LIST 자료확인  --- 횡방향 순서대로 rows를 기록한다.
rows.insert(0, title)  # Header를 끼워 넣는다.

write_excel(rows, filename_with_dir)
