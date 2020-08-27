"""
# functions : for a few initial path setting
"""
print(__doc__)

import os
import sys

from typing import List


NAME_HOME = 'openCV_TAcademy'


def get_cut_dir(name_cut:str) -> str:
    dir_current = os.path.dirname(__file__)
    dir_cut = "".join(dir_current.partition(name_cut)[:2])
    return dir_cut

def stop_if_none(object:object, message:str) -> object:
    """# 오브젝트 로딩 실패 시(None), 시스템(sys.exit) 종료"""
    if object is None:
        if not message:
            print(f"*** object loading failed! '{object}' -> stop system!")
        else:
            print(f"*** {message}")

        sys.exit()
    else:
        return object

def echo(echoes:List) -> None:
    """# _path 화일에 대한 설명 에코 : 필요 없을 수 도... """
    if not echoes:                          # default echo
        echoes = [
            '*** dir_home 이 글로벌 변수로 선언 되었습니다.',
            '*** dir_home 이 시스템 Path의 첫번째에 등록 되었습니다.',
            f'  : dir_home = {dir_home}',
        ]


    [print(echo) for echo in echoes]


DIR_HOME = get_cut_dir(NAME_HOME) + '\\'
sys.path.insert(0, DIR_HOME)


DIR_SRC = DIR_HOME + 'src\\'
DIR_OCR = DIR_SRC + 'easyOCR\\'
