"""
* 엑셀작업 줄이기 - 엑셀없이 코드로 수정/정리/추출/쓰기
* 보안 잠금된 화일은 안됨 = 읽기/쓰기(코딩) = 조회(엑셀)
* OpenPyXL = xlsx 지원, 읽기/쓰기
* XlsxWriter (화일생성, 서버사이드) = xlsx 지원
* Xlrd, Xlwt, xlwings, pywin32 = xls 지원 (Win, Mac, Linux)
* xlwings (W,M), pywin32 (W) - 설치된 엑셀필요
"""
# script run 에서는 실행이 안됨.
import random as rd
import openpyxl as opx

from pprint import pprint

# 자료만들기 4행5열 데이터
names = ['PARK', 'LEE', 'KIM', 'CHOI', 'LIM', 'YU', 'CHEONG', 'SEO']
title = ['NAME', 'KOR', 'ENG', 'MATH', 'REMARK', ]
rows = []

for i, name in enumerate(names):
    scores = []
    for j in range(len(title) - 2):
        score = rd.randrange(40, 100, 5)
        scores.append(score)

    rows.append([name, scores[0], scores[1], scores[2], '-', ])

# 만들어진 LIST 자료확인
pprint(rows)

OUT_XLSX = "./_static/_write.xlsx"
WB = opx.Workbook()
WS = WB.active

# 타이틀기록
WS.append(title)

# 데이터 기록
for row in rows:
    WS.append(row)


# 엑셀 파일 저장
WB.save(OUT_XLSX)
WB.close()
