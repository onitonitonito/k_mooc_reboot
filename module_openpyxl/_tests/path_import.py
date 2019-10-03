"""
# 서브폴더에서 상위폴더 지정하는 테스트
# 터미널/스크립트-런 에서 인식하는 결과가 차이가 나서...
"""
# print(__doc__)

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


import _assets.script_run
from _assets import configs




def main():
    # [print(path) for path in sys.path]
    configs.main()
    pass


if __name__ == '__main__':
    main()
