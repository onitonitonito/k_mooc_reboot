"""
# 엑셀작업 줄이기 - 엑셀없이 코드로 수정\\정리\\추출\\쓰기
# OpenPyXL = xlsx 지원, 읽기\\쓰기
# XlsxWriter (화일생성, 서버사이드) = xlsx 지원
# Xlrd, Xlwt, xlwings, pywin32 = xls 지원 (Win, Mac, Linux)
# xlwings (W,M), pywin32 (W) - 설치 된 엑셀필요
"""
# script run 에서는 실행이 안됨.

import pandas as pd
import openpyxl as opx
import _assets.script_run

from _assets.configs import *
from _assets.classes import *


# 같은 내용 다른 포맷
TARGET_READ = join_dir(
    get_dir(dir_top, dir_dict, "_statics"),
    '_result.xlsx',
)
OUTPUT_01 = join_dir(
    get_dir(dir_top, dir_dict, "_results"),
    '_u_even.xls',
)
OUTPUT_02 = join_dir(
    get_dir(dir_top, dir_dict, "_results"),
    '_u_odd.xls',
)

WB = opx.load_workbook(TARGET_READ)
WS = WB["Sheet"]
# sheet = wb.get_sheet_by_name("Sheet1")        # deprecated


def excel_read_split_out(read, out1, out2):
    """
    * DOCS::pandas.read_excel = https:/goo.gl/Dy1A5z
    # target 을 읽어 들여서 ... pandas xls (output_01, 02) 로 나누어 저장.
    """
    # read target file as pandas df
    df = pd.read_excel(read)
    print(df)           # for TEST

    # rows_even
    df[0::2].to_excel(out1)

    # rows_odd
    df[1::2].to_excel(out2)


def show_cells(sheet):
    """
    # print(sheet['A1'].value, sheet['B1'].value)
    """
    print(f"active cell(now)    : '{sheet.active_cell}'")
    print(f"  - min/max rows    : {sheet.min_row} ~ {sheet.max_row}")
    print(f"  - min/max columns : {sheet.min_column} ~ {sheet.max_column}")
    print(f"  - active range    : {sheet.calculate_dimension()}")
    print()

    for i in range(1, sheet.max_row + 1):
        cell_01 = sheet[f"A{i}"].value
        cell_02 = sheet[f"B{i}"].value
        print(f"{cell_01:>10} : {cell_02}")

    print()
    print(f"[1,1] = {sheet.cell(1, 1).value}")
    print(f"[1,2] = {sheet.cell(1, 2).value}")


def show_overview(sheet):
    """
    # 전체 입력 란을 오버뷰
    """
    for row in sheet.rows:
        # print(type(row[5]))
        # print([col.col_idx for col in row])
        # print([col.value for col in row])
        print(row[-3].value)
        pass
    # [print(func) for func in dir(row[5]) if not func.startswith('_')]


def main():
    print(excel_read_split_out.__doc__)
    excel_read_split_out(TARGET_READ, OUTPUT_01, OUTPUT_02)

    print(show_cells.__doc__)
    show_cells(WS)

    print(show_overview.__doc__)
    show_overview(WS)


if __name__ == '__main__':
    main()
