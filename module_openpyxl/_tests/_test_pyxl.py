"""
# 서브폴더에서 상위폴더 지정하는 테스트
# 터미널/스크립트-런 에서 인식하는 결과가 차이가 나서...
"""
import os
import sys

def get_dir_by_name(name_top):
    """
    top level name을 기준으로 dir을 반환한다.
    사용환경에 따라, 실행기준이 달라지기 때문에
    탑레벨을 시스템 path 에 추가한다.
    """
    dir_array = os.getcwd().partition(name_top)
    dir_by_name = "".join(dir_array[:2])
    return dir_by_name

name_top = 'k_mooc_reboot'
name_work = "module_openpyxl"

dir_top = get_dir_by_name(name_top)
dir_work = os.path.join(dir_top, name_work)

sys.path.insert(0, dir_work)   # insert at the top
# [print(path) for path in sys.path]  # for test
# --------------------------------------------------------------------------

"""
# 엑셀작업 줄이기 - 엑셀없이 코드로 수정/정리/추출/쓰기
# 보안 잠금된 화일은 안됨 = 읽기/쓰기(코딩) = 조회(엑셀)
"""
# OpenPyXL = xlsx 지원, 읽기/쓰기
# XlsxWriter (화일생성, 서버사이드) = xlsx 지원
# Xlrd, Xlwt, xlwings, pywin32 = xls 지원 (Win, Mac, Linux)
# xlwings (W,M), pywin32 (W) - 설치된 엑셀필요
# script run 에서는 실행이 안됨.

import pandas as pd
import openpyxl as opx
import _assets.script_run

import matplotlib.pyplot as plt

# TARGET_XLS = "./_statics/_total_example.xls"
# OUTPUT_01 = "./_statics/_u_even.xls"
# OUTPUT_02 = "./_statics/_u_odd.xls"

# TARGET_XLSX = "./_statics/hydrauric_sheet.xlsx"  # security locked-impossible
TARGET_XLSX = "./_statics/_sample.xlsx"          # not

WB = opx.load_workbook(TARGET_XLSX)
SHEET = WB['Sheet']


# cell_obj 호출 = SHEET['A1'].value
# print(SHEET['A2'].value)

for row in SHEET.rows:
    # row is tuple which consist of cell_obj
    # print(row[0].value)

    rows = [col.value for col in row]
    print(rows)
