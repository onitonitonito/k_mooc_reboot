"""
# 08장 Jump to Python 종합문제 - 문제풀이에 사용되는 모듈
# - 문제.10번 = Calculator()
#
"""
# print(__doc__)

import re
import numpy as np


class IoReadWrite(object):
    """ READ / WRITE 객체 오픈 & 클로즈
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


class Calculator(object):
    """ 문제10번 사칙연산 계산기 -클래스 Calculator 문제
        - 객체호출시 계산대상을 array 로 입력
        - ex. cal = Calculator(array_int=[])
    """

    def __init__(self, array_int):
        self.array_int = array_int

    def sum(self):
        return np.sum(a=self.array_int)

    def avg(self):
        return np.average(a=self.array_int)


class DashInsert(object):
    """ 문제13번 DashInsert 문제
        - 숫자스트링 받아서 연속홀수/연속짝수 사이 구분기호 삽입
    """

    def is_odd(self, number_int):
        return (number_int % 2) is 1

    def is_even(self, number_int):
        return (number_int % 2) is 0

    def get_dash_inserted(self, number_int):
        array_number_str = [num for num in str(number_int)]
        array_inserted_str = []

        i = 0
        while i < len(array_number_str) - 1:
            n = int(array_number_str[i])
            n_after = int(array_number_str[i + 1])

            # print(n,n_after)
            if self.is_even(n) and self.is_even(n_after):
                array_inserted_str.append(f"{n}*")

            elif self.is_odd(n) and self.is_odd(n_after):
                array_inserted_str.append(f"{n}-")

            else:
                array_inserted_str.append(f"{n}")

            i += 1

        array_inserted_str.append(array_number_str[-1])

        return (''.join(array_inserted_str))


class CompressString(object):
    """ 문제14번 반복문자열 압축문제
        - 반복되는 글자수를 세어 숫자로 덧붙인다, 1개도 적용
    """

    def get_str_compressed(self, input_str):
        array_input_str = [char for char in input_str]
        array_compressed_str = []                # 가공해서 담을 바구니 준비!
        count_char = 1

        for i, char in enumerate(array_input_str):
            if i < (len(array_input_str)-1):     # 마지막 글자가 아니면,
                if char is array_input_str[i+1]: # (뒷 글자)와 비교
                    count_char += 1              # 같으면 +1 키운트

                else:                            # 다르면 기록하고, 카운트 리셋
                    array_compressed_str.append(char + str(count_char))
                    count_char = 1
                                                 # IndexError 방지를 위해서,
            else:                                # 마지막 글자인 경우
                if char is array_input_str[i-1]: # (앞 글자)와 비교 (에러방지)
                    array_compressed_str.append(char + str(count_char))
                                                 # 같으면 바로 기록
                else:                            # 다르면 1개로 기록, 리셋(x)
                    array_compressed_str.append(char + "1")

        compressed_str = ''.join(array_compressed_str)
        return input_str, compressed_str


class DuplicateNumber(object):
    """ 문제15번 Duplicate Numbers 압축문제
        - 0~9 숫자중 한번이상 반복되는지 판단한다
        - 한번씩 사용 했는지, 점검한다
    """
    def get_set_array(self, number_str):
        array_number_int = [int(num) for num in number_str]
        array_set_int = set(array_number_int)
        return array_set_int


    def get_length_original_vs_set(self, number_str):
        set_array = self.get_set_array(number_str)
        return len(number_str), len(set_array)


    def get_array_splited_space(self, array_number_str_space):
        array_splited_space = array_number_str_space.split(' ')
        return array_splited_space


class MorseConvert(object):
    """ 문제16번 모스부호 해독 문제
    - upper case str 을 입력받아 morse str을 반환
    """

    def __init__(self):
        self.dict_morse = {
        'A':	'.-',
        'B':	'-...',
        'C':	'-.-.',
        'D':	'-..',
        'E':	'.',
        'F':	'..-.',
        'G':	'--.',
        'H':	'....',
        'I':	'..',
        'J':	'.---',
        'K':	'-.-',
        'L':	'.-..',
        'M':	'--',
        'N':	'-.',
        'O':	'---',
        'P':	'.--.',
        'Q':	'--.-',
        'R':	'.-.',
        'S':	'...',
        'T':	'-',
        'U':	'..-',
        'V':	'...-',
        'W':	'.--',
        'X':	'-..-',
        'Y':	'-.--',
        'Z':	'--..',
        '_':    ' ',
        }

        def get_morse_from_str(self, upper_str):
            array_upper_str = [char for char in upper_str]

            array_morse = [
            self.dict_morse[key]
            if key is not ' ' else self.dict_morse['_']
            for key in array_upper_str]

            return ' '.join(array_morse)

            def get_str_from_morse(self, morse_str):
                array_morse_str = morse_str.split(' ')

                _d_keys = list(self.dict_morse.keys())
                _d_vals = list(self.dict_morse.values())

                array_char_str = [_d_keys[_d_vals.index(char)]
                if char is not '' else '_'
                for char in array_morse_str]

                char_str = ''.join(array_char_str).replace('__', ' ')
                return char_str


class RegularExprssion(object):
    """ 문제19번 정규표현식 그루핑 문제
    - 정규표현식 패턴객채(p)를 생성한다
    - 타켓스트링 매치객체(m)울 생성한다
    """

    def get_re_pattern(self):
        pass




if __name__ == '__main__':


    pass
