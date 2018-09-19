"""
* 엑셀작업 줄이기 - 엑셀없이 코드로 수정/정리/추출/쓰기
* OpenPyXL = xlsx 지원, 읽기/쓰기
* XlsxWriter (화일생성, 서버사이드) = xlsx 지원
* Xlrd, Xlwt, xlwings, pywin32 = xls 지원 (Win, Mac, Linux)
* xlwings (W,M), pywin32 (W) - 설치된 엑셀필요
"""
# script run 에서는 실행이 안됨.

import pandas as pd
import openpyxl as opx

# 같은 내용 다른 포맷
TARGET_XLSX = "./_static/_new_example.xlsx"
TARGET_XLS = "./_static/_new_example.xls"

OUTPUT_01 = "./_static/_u_even.xls"
OUTPUT_02 = "./_static/_u_odd.xls"

WB = opx.load_workbook(TARGET_XLSX)
SHEET = WB["Sheet1"]
# sheet = wb.get_sheet_by_name("Sheet1")        # deprecated


def excel_inout(target, out1, out2):
    """
    * DOCS::pandas.read_excel = https://goo.gl/Dy1A5z
    """
    df = pd.read_excel(target)
    df[0::2].to_excel(out1)
    df[1::2].to_excel(out2)


def show_cell(sheet):
    """
    * print(sheet['A1'].value, sheet['B1'].value)
    """
    for i in range(1, 30):
        print(sheet['A' + str(i)].value, " = ", sheet['B' + str(i)].value)

    print()
    print("[1,1] =", sheet.cell(row=1, column=1).value)
    print("[1,2] =", sheet.cell(row=1, column=2).value)


def show_overview(sheet):
    """전체 입력란을 오버뷰"""
    for row in sheet.rows:
        print([col.value for col in row])


if __name__ == '__main__':
    excel_inout(TARGET_XLS, OUTPUT_01, OUTPUT_02)
    # show_cell(SHEET)
    # show_overview(SHEET)
