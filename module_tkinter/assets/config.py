"""
# config.py - 전체 변수, dir 구조에 대하여 관리한다.
"""
import os
import sys

print(__doc__)


# 폴더 구조관련 변수
dir_top = "module_tkinter"
dir_array = os.path.dirname(__file__).partition(dir_top)
dir_root = "".join(dir_array[:2]) + "\\"

dir_assets = dir_root + "assets\\"
dir_statics = dir_root + "statics\\"
dir_logging = dir_root + "logging\\"

dir_img = dir_statics + "images\\"
dir_results = dir_statics + "results\\"


# 기본 변수
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 550
HORZ_MOVE = 1
VERT_MOVE = 1
JUMP_DURATION = 20
FLIP_SECOND = 0.01 * 5        # default = 0.01(너무빠름)


if __name__ == '__main__':
    # for TEST ... dir_root 변수만 필요 함 (가공하기 위한 과정)
    print(dir_root)
    print(dir_assets)
    print(dir_statics)
    print(dir_logging)
