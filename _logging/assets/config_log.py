"""
# config_log.py - 변수를 입력합니다.
#
"""
import os, sys

print(__doc__)

name_top = "_logging"
dir_array = os.path.dirname(__file__).partition(name_top)

dir_root = "".join(dir_array[:2]) + "\\"
dir_src = dir_root + "src\\"
dir_assets = dir_root + "assets\\"
dir_log = dir_root + "log\\"




if __name__ == '__main__':
    # for TEST ... dir_root 변수만 필요 함 (가공하기 위한 과정)
    print(dir_root)
    print(dir_src)
    print(dir_log)
    print(dir_assets)
    
