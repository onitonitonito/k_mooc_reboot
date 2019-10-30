"""
# assets/classes.py - 공동으로 사용하는 함수 모음
"""
print(__doc__)




def write_excel(array_2d, filename_with_dir):
    """새로운 엑셀화일 생성하기"""
    import openpyxl as opx
    # # 1열에 타이틀기록
    # WS.append(title)
    #
    # # 다음 열에서 부터 데이터(rows)를 반복 기록
    # for row in rows:
    #     WS.append(row)

    # 워크북 / 워크시트를 설정한다.
    WB = opx.Workbook()
    WS = WB.active

    for row in array_2d:
        WS.append(row)

    # 작성된 엑셀 파일을 저장
    WB.save(filename_with_dir)
    WB.close()
