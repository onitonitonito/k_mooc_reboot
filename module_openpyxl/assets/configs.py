"""
# assets/configs.py - 각종변수 및 Paths를 지정
"""
import os
import sys
from typing import Dict

print(__doc__)

name_root = "k_mooc_reboot"
name_home = "module_openpyxl"




def main():

    pass

def abspath_by_name(dir_name:str) -> str:
    """get abspath(absolute path) cut util given 'dir_name'"""
    dir_hereent = os.path.dirname(__file__)
    dirs = dir_hereent.partition(dir_name)
    dir_cut_combined = "".join(dirs[:2]) + "\\"
    return dir_cut_combined

def set_vars_from_dict(dict_obj: Dict) -> None:
    """make global vars. from dict"""
    for key, val in dict_obj.items():
        globals()[key] = dict_obj[key]

def show_dict_items(dict_obj: Dict) -> None:
    print(" "*7 + "KEYS" + " "*15 + "VALUES")
    print("------" * 10)
    for _key, _val in dict_obj.items():
        print(f"{_key:16} : {_val}")
    print("------" * 10, "\n\n")


paths = {
    'dir_root' : abspath_by_name(name_root),
    'dir_home' : abspath_by_name(name_home),

    'dir_assets' : abspath_by_name(name_root) + '_assets\\',
    'dir_statics': abspath_by_name(name_root) + '_statics\\',
    'dir_logging': abspath_by_name(name_root) + '_logging\\',

    'dir_home_assets' : abspath_by_name(name_home) + 'assets\\',
    'dir_home_statics': abspath_by_name(name_home) + 'statics\\',
    'dir_home_tests'  : abspath_by_name(name_home) + 'tests\\',
    'dir_home_works'  : abspath_by_name(name_home) + 'works\\',
    }

# 딕셔너리값으로 변수를 셋팅한다
set_vars_from_dict(paths)

show_dict_items(paths)


if __name__ == '__main__':
    main()
