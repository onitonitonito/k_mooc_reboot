"""
# 엑셀작업 줄이기 - 엑셀없이 코드로 수정/정리/추출/쓰기
# 보안 잠금된 화일은 안됨 = 읽기/쓰기(코딩) = 조회(엑셀)
#  - 새로운 엑셀형식 화일만들기
"""
# script run 에서는 실행이 안됨 = 이것은 '케바케'
# print(__doc__)

import random
import _assets.script_run

from _assets.configs import *
from _assets.classes import *


filename = "_write.xlsx"
filename_with_dir = join_dir(
                get_dir(dir_top, dir_dict, "_staticss"),
                filename,
                )


# 자료만들기 4행5열 데이터
title = ['NAME', 'KOR', 'ENG', 'MATH', 'REMARK', ]
names = ['PARK', 'LEE', 'KIM', 'CHOI', 'LIM', 'YU', 'CHEONG', 'SEO']

rows = []
for name in names:
    scores = []
    for i in range(3):
        score_random = random.randrange(40, 100, 5)
        scores.append(score_random)

    rows.append([name, *scores, '-', ])

# 만들어진 LIST 자료확인  --- 횡방향 순서대로 rows를 기록한다.
# print(rows)     # for test

echos = rows.insert(0, title)


write_excel(rows, filename_with_dir)
