"""
# INPUT 시트의 내용을 기준으로 OUTPUT 템플릿에 내용을 기록
# 먼저 같은 WBI의 'TEST' 텝에 먼저 기록 테스트.
"""
import pandas as pd
import openpyxl as ox
import assets.script_run

from assets.configs import *

print(__doc__)

TARGET_READ = dir_home_statics + 'target_input.xlsx'
OUT_DESIGNATED = dir_home_works + 'target_output.xlsx'

# 미리 만들어 놓은 시트이름 INPUT, TEST.
WBI = ox.load_workbook(TARGET_READ)
WSI_01 = WBI["INPUT"]
WSI_02 = WBI["TEST"]

# Sheet 이름은 존재하는 탭 이름을 써야 함.
WBO = ox.load_workbook(OUT_DESIGNATED)
# WSO_01 = WBO["Sheet1"]
# WSO_02 = WBO["Sheet2"]
WSO_03 = WBO["Sheet3"]



def main():
    show_overview(WSI_01)
    print()

    show_all(WSO_03); quit()

    # [print(row) for row in get_WS_array(WSI_01)]  # ... for TEST!
    ws_array = get_WS_array(WSI_01)
    df = pd.DataFrame(data=ws_array)

    print(df)

    df.to_excel(excel_writer=OUT_DESIGNATED, index=False, header=False, )

    # TODO: 추가 탭 쓰기가 되지 않고, 탭 하나에 덮어쓴다 (추가탭 쓰기 필요)
    # df.to_excel(excel_writer=OUT_DESIGNATED, sheet_name="Sheet2")
    # df.to_excel(excel_writer=OUT_DESIGNATED, sheet_name="Sheet3")


    # # WSI_01 입력내용을 array 를 만든다.
    # WSI_01_array = get_WS_array(WSI_01)
    #
    # # WSI_01_array의 내용을, WSI_02에 기록하고 WBI를 저장한다.
    # set_array_to_WS(WSI_01_array, WSI_02)
    # WBI.save(TARGET_READ)
    #
    #
    # # WSI_01_array의 내용을, WSO_01~03 반복해서 기록하고 WBO를 저장한다.
    # set_array_to_WS(WSI_01_array, WSO_01)
    # set_array_to_WS(WSI_01_array, WSO_02)
    # set_array_to_WS(WSI_01_array, WSO_03)
    # WBO.save(OUT_DESIGNATED)



def set_array_to_WS(WS_array, WS_target):
    """
    # WS_array 형식 = column : [[CELL_NAME, TEXT, NUMBER, EQUATION], ]
    # _blank = None, 3개중 1개만 채운다.
    """
    for rows in WS_array:
        cell_name = rows[0]

        if cell_name.startswith('CELL'):  # 해더는 패스!
            continue

        if rows[1]:
            WS_target[cell_name] = rows[1]
            print(f"WS[{cell_name}] = str({rows[1]})")

        elif rows[2]:
            WS_target[cell_name] = int(rows[2])
            print(f"WS[{cell_name}] = int({rows[2]})")

        elif rows[3]:
            WS_target[cell_name] = rows[3]
            print(f"WS[{cell_name}] = str({rows[3]})")
    print(f"*** WRITING worksheet is Done! '{len(WS_array)-1}' times ***\n\n")

def get_WS_array(worksheet):
    """WS 를 입력하면 입력된 범위 만큼의 str_array를 만든다"""
    # ws_array = []
    # for i, row in enumerate(worksheet.rows):
    #     ws_array.append([])
    #     for col in row:
    #         ws_array[i].append(f"{col.value}")

    # ALL THE SAME
    ws_array = []
    for row in worksheet.rows:
        ws_array.append([col.value for col in row])
    return ws_array

def show_all(worksheet):
    # ALL THE SAME! ... 1-line coding!.. apprehansive repeat!
    # [print(f"{col.value}, ", end="\n")
    #     if i%4 == 3
    #     else print(f"{col.value}, ", end="")
    #     for row in WSI_01.rows
    #     for i, col in enumerate(row)]

    # 전체 값 둘러보기 (pos_xy에서 개별 가져오기)
    # for row in WSI_01.rows:
    #     for col in row:
    #         print(f"{col.value}, ", end="")
    #     print()

    # 1 row(tuple) 가져오기
    for row in worksheet.rows:
        for i, col in enumerate(row):
            if i % 4 == 3:
                print(f"{col.value}")       # 마지막 4칼럼에서 줄바꿈
            else:
                print(f"{col.value}, ", end='')

def show_overview(sheet):
    """
    # 전체 입력 란을 오버뷰
    """
    for row in sheet.rows:
        # # <class 'openpyxl.cell.cell.Cell'>
        # print(type(row[2]))

        # # [1, 2, 3, 4, 5, 6] ... Index는 항상일정
        # print([col.col_idx for col in row])

        # # 뒤에서 3번째 칼럼 = MATH
        # print(row[0].value)

        # ['NAME', 'KOR', 'ENG', 'MATH', 'SUM', 'AVERAGE']
        print([col.value for col in row])



if __name__ == '__main__':
    main()
