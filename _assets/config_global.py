"""
# config_global.py - 전체 변수를 입력합니다.
#
"""
import os, sys

print(__doc__)

dir_top = "k_mooc_reboot"
dir_array = os.path.dirname(__file__).partition(dir_top)
dir_root = "".join(dir_array[:2]) + "\\"

dir_assets = dir_root + "_assets\\"
dir_statics = dir_root + "_statics\\"
dir_logging = dir_root + "_logging\\"

dir_pickle = dir_statics + "_pickle\\"


if __name__ == '__main__':
    # for TEST ... dir_root 변수만 필요 함 (가공하기 위한 과정)
    print(dir_root)
    print(dir_assets)
    print(dir_statics)
    print(dir_logging)
