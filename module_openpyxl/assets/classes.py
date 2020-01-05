"""
# assets/classes.py - 공동으로 사용하는 함수 모음
"""

import openpyxl as opx

print(__doc__)

def write_excel(array_2d, filename_with_dir):
    """새로운 엑셀화일 생성하기"""
    # 워크북 / 워크시트를 설정한다.
    WB = opx.Workbook()
    WS = WB.active

    for row in array_2d:
        WS.append(row)

    # 작성된 엑셀 파일을 저장
    WB.save(filename_with_dir)
    WB.close()


def show_commands(obj):
    print(f"\n\nCOMMANDS LIST for {obj}")
    print('--------' * 5)
    command_list = obj.__dir__()
    for i, item in enumerate(command_list):
        if not item.startswith("_"):
            print(f" {i+1:02}.", item)
    print('--------' * 5)
