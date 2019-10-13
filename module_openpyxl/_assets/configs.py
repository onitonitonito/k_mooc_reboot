"""
# _assets/configs.py - 각종변수 및 Path를 지정
"""
import os
import sys

print(__doc__)

def get_dir_by_name(name_top):
    """
    top level name을 기준으로 dir을 반환한다.
    사용환경에 따라, 실행기준이 달라지기 때문에
    탑레벨을 시스템 path 에 추가한다.
    """
    dir_array = os.getcwd().partition(name_top)
    dir_by_name = "".join(dir_array[:2])
    return dir_by_name

def join_dir(*dirs_array):
    return os.path.join(*dirs_array)

def get_dir(dir_top, dir_dict, key_name):
    return os.path.join(dir_top, *dir_dict[key_name])



name_top = "k_mooc_reboot"
dir_top = get_dir_by_name(name_top)
dir_dict = {
    '_assets' : ['module_openpyxl', '_assets',],
    '_results' : ['module_openpyxl', '_results',],
    '_staticss' : ['module_openpyxl', '_staticss',],
    '_tests' : ['module_openpyxl', '_tests',],
}




def main():
    print("top :", dir_top)
    print("_assets :", get_dir(dir_top, dir_dict, "_assets"))
    print("_tests :", get_dir(dir_top, dir_dict, "_tests"))

if __name__ == '__main__':
    main()
