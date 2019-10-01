"""
# 엑셀작업 줄이기 - 엑셀없이 코드로 수정/정리/추출/쓰기
# 보안 잠금된 화일은 안됨 = 읽기/쓰기(코딩) = 조회(엑셀)
"""
# OpenPyXL = xlsx 지원, 읽기/쓰기
# XlsxWriter (화일생성, 서버사이드) = xlsx 지원
# Xlrd, Xlwt, xlwings, pywin32 = xls 지원 (Win, Mac, Linux)
# xlwings (W,M), pywin32 (W) - 설치된 엑셀필요
# script run 에서는 실행이 안됨.

import openpyxl as opx
import pandas as pd
import matplotlib.pyplot as plt

# TARGET_XLS = "./_static/_total_example.xls"
# OUTPUT_01 = "./_static/_u_even.xls"
# OUTPUT_02 = "./_static/_u_odd.xls"

# TARGET_XLSX = "./_static/hydrauric_sheet.xlsx"  # security locked-impossible
TARGET_XLSX = "./_static/_sample.xlsx"          # not

WB = opx.load_workbook(TARGET_XLSX)
SHEET = WB['Sheet']


# cell_obj 호출 = SHEET['A1'].value
# print(SHEET['A2'].value)

for row in SHEET.rows:
    # row is tuple which consist of cell_obj
    # print(row[0].value)

    rows = [col.value for col in row]
    print(rows)
