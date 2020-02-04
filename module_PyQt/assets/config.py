"""
# config.py - 변수를 입력합니다.
#
"""
import os, sys

print(__doc__)

dir_top = "module_PyQt"
dir_array = os.path.dirname(__file__).partition(dir_top)
dir_root = "".join(dir_array[:2]) + "\\"

dir_assets = dir_root + "assets\\"
dir_statics = dir_root + "statics\\"

dir_icon = dir_statics + "icons\\"
dir_img = dir_statics + "images\\"


if __name__ == '__main__':
    # for TEST ... dir_root 변수만 필요 함 (가공하기 위한 과정)
    print(dir_root)
    print(dir_assets)
    print(dir_statics)
    print(dir_logging)
