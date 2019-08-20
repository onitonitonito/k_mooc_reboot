"""
# 08장 Jump to Python 종합문제 - 문제풀이에 사용되는 모듈
# - 문제.10번 = Calculator()
#
"""
# print(__doc__)

import numpy as np


class Calculator(object):
    """ 문제10번 계산기 모듈사용
        - 객체호출시 계산대상을 array 로 입력
        - ex. cal = Calculator(array_int=[])
    """

    def __init__(self, array_int):
        self.array_int = array_int

    def sum(self):
        return np.sum(a=self.array_int)

    def avg(self):
        return np.average(a=self.array_int)


class IoReadWrite(object):
    """ READ / WRITE 객체 오픈&클로즈
    - read_assign(filename_with_dir)
    - write_to_file(filename_with_dir, bundle_str)
    """

    def read_assign(filename_with_dir):
        """ 화일에서 읽어와서 return 한다.
        -> 파일명, 파일위치
        <- return 텍스트 스트링(번들)
        """
        with open(file=filename_with_dir, mode='r', encoding='utf8') as f:
            bundle_str = f.read()
        return bundle_str

    def write_to_file(filename_with_dir, bundle_str):
        """ 스트링을 받아서 화일이름으로 기록한다.
        -> 파일명, 파일위치
        -> 텍스트 스트링(번들)
        () 기록한다, utf8
        <- return 'ok'
        """
        with open(file=filename_with_dir, mode='w', encoding='utf8') as r:
            r.write(bundle_str)
        return True


if __name__ == '__main__':
    pass
