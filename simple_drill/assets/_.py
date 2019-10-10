"""
# getcwd, __file__ 로 dir 검출해 내기 비교
"""
# CMD와 스크립트 런에서 결과가 달라 짐 / 주피터노트북에서 사용 못함
from os import getcwd, path
print(__doc__)

dir_file = __file__.split("\\")
dir_working = "\\".join(dir_file[:-1])

def main():
    run_01()
    run_02()
    run_03()

def run_01():
    """
    # getcwd()는 (1) cmd와 (2) 스크립트런에서 결과가 다름
    # (1) C:/Users/ ... /k_mooc_reboot/simple_drill/assets
    # (2) C:/Users/ ... /k_mooc_reboot
    """
    print(getcwd())

def run_02():
    """
    # split / join - __file__ 은 정확한데, Jupyter notebook 사용 불가능!
    """
    print(dir_file)
    print(dir_working)

def run_03():
    """
    # os.path.join - 이렇게 쓰면 C:Users/ ... /assets  (C://이 삭제 됨)
    """
    print(path.join(*dir_file[:-1]))


if __name__ == '__main__':
    main()
