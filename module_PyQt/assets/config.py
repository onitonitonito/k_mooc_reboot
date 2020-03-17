"""
# config.py - DEFINE & REGISTER FOLDER STRUCTURE of APP
"""
import os, sys

print(__doc__)

name_home = "module_PyQt"

dir_array = os.path.dirname(__file__).partition(name_home)
dir_home = "".join(dir_array[:2]) + "\\"

dir_assets = dir_home + "assets\\"
dir_statics = dir_home + "statics\\"

dir_icon = dir_statics + "icons\\"
dir_img = dir_statics + "images\\"
dir_ui = dir_statics + "uis\\"
dir_ini = dir_statics + "inis\\"


if __name__ == '__main__':
    # for TEST ... dir_root 변수만 필요 함 (가공하기 위한 과정)
    import config
    [print(f"{key:12} : ...{val[20:]}")
                for key, val in config.__dict__.items()
                if key.startswith('dir')]
