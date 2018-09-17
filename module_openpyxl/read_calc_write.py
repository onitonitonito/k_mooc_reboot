"""
* 엑셀작업 줄이기 - 엑셀없이 코드로 수정/정리/추출/쓰기
* 보안 잠금된 화일은 안됨 = 읽기/쓰기(코딩) = 조회(엑셀)
* OpenPyXL = xlsx 지원, 읽기/쓰기
* XlsxWriter (화일생성, 서버사이드) = xlsx 지원
* Xlrd, Xlwt, xlwings, pywin32 = xls 지원 (Win, Mac, Linux)
* xlwings (W,M), pywin32 (W) - 설치된 엑셀필요
"""
# script run 에서는 실행이 안됨.

import openpyxl as opx

IN_XLSX = "./_static/_write.xlsx"
OUT_XLSX = "./_static/_result.xlsx"

# 엑셀파일 열기 (WB = Working Book)
WB = opx.load_workbook(IN_XLSX)
WS = WB.active

# 국영수 점수를 읽기
for i, r in enumerate(WS.rows, 1):
    row_index = r[0].row   # 행 인덱스
    kor = r[1].value
    eng = r[2].value
    math = r[3].value

    if isinstance(kor, int):
        sum = "=SUM(B{0}:D{0})".format(i)
        average = "=ROUND(AVERAGE(B{0}:D{0}), 0)".format(i)
    elif isinstance(kor, str):
        sum, average = "SUM", "AVERAGE"
    else:
        sum = average = "... NoneType!!"

    # 합계 쓰기
    WS.cell(row=row_index, column=5).value = sum
    WS.cell(row=row_index, column=6).value = average

    print(kor, eng, math, sum, average)

WS.append(['TOTAL SUM',
           '=SUM(B2:B9)', '=SUM(C2:C9)', '=SUM(D2:D9)',
           '=ROUND(AVERAGE(E2:E9), 0)',
           '=ROUND(AVERAGE(F2:F9), 0)', ])

# 엑셀 파일 저장
WB.save(OUT_XLSX)
WB.close()
