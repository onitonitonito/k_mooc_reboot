"""
# assets/configs.py - 각종변수 및 Paths를 지정
"""
import os
import sys

print(__doc__)

name_root = "k_mooc_reboot"
name_home = "module_matplotlib"

def main():
    pass

def abspath_by_name(dir_name):
    """get abspath(absolute path) cut by given 'dir_name'"""
    dir_current = os.path.dirname(__file__)
    dir_cuts = dir_current.partition(dir_name)
    dir_cut = "".join(dir_cuts[:2]) + "\\"
    return dir_cut

def set_vars_from_dict(dict_obj):
    """make global varis. from dict"""
    for key, val in dict_obj.items():
        globals()[key] = dict_obj[key]

def show_dict_items(dict_obj):
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
    'dir_home_imgproc': abspath_by_name(name_home) + 'image_processing\\',
    }

# 딕셔너리값으로 변수를 셋팅한다
set_vars_from_dict(paths)




if __name__ == '__main__':
    main()
