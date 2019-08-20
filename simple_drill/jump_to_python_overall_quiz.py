"""
# 08장 종합문제 - Jump to Python
#
# https://wikidocs.net/17114
# 파이썬은 웹, GUI, 네트워크, 딥러닝 등 상당히 많은 일을 할 수 있는 언어이다.
  - 여러분이 지금까지 배운 내용을 충분히 숙지했다면 이제 이들을 향해 첫발을 내디딜
  - 준비를 마친 것이다. 하지만 그전에 여기에 준비한 문제들을 풀어 보면서 여러분이
  - 얼마나 파이썬에 익숙해졌는지 점검해 보도록 하자.

# (종합문제 풀이 : https://wikidocs.net/12769#08)
\n\n\n"""
# print(__doc__)

class ExamFinal(object):
    """ 점프 투 파이썬 최종 종합문제 """
    def q01(self):
        """ Q1 문자열 바꾸기 - split와 join 함수사용 다음과 같이 고치시오.
        a:b:c:d --> a#b#c#d
        """
        _a = "a:b:c:d"
        _a_splits = _a.split(":")        # [,,,,]
        _a_join = "#".join(_a_splits)
        return _a, _a_join


    def q02(self, key):
        """ Q2 딕셔너리 값 추출하기
        a 딕셔너리에는 'C'라는 key가 없으므로 위와 같은 오류가 발생한다.
        'C'에 해당하는 key 값이 없을 경우 오류 대신 70을 얻을 수 있도록 수정.
        """
        _a = {'A': 90, 'B': 80}

        try:
            return _a[key]
        except:
            return "70 --> ** exceptional return without dict_key"


    def q03(self, ):
        """ Q3 리스트의 더하기와 extend 함수 - 두기능의 차이를 설명하시오
        >>> a = [1, 2, 3]
        >>> a = a + [4,5]
        >>> a = [1, 2, 3, 4, 5]

        >>> a.extend([4, 5])
        >>> a = [1, 2, 3, 4, 5]
        """
        _a = [1, 2, 3]
        _a_plus = _a + [4, 5]          # 어싸인 값이 있다
        _a_ext = _a.extend([4, 5])     # 어사인 값이 없다 ... return None

        # extend() 는 None을 반환하며, a 자체를 수정한다.
        return _a, _a_plus, _a_ext


    def q04(self, ):
        """ Q4 리스트 총합 구하기
        A학급 학생점수 리스트. 50점 이상 점수 총합을 구하시오.
        A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
        """
        scores = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

        (total_every, total_over_50) = (0, 0)
        for score in scores:
            total_every += score
            if score > 50:
                total_over_50 += score

        return total_every, total_over_50


    def q05(self, n):
        """ Q5 피보나치 함수
        첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후에 이어지는 항은
        이전의 두 항을 더한 값으로 이루어지는 수열을 피보나치 수열이라고 한다
        0, 1, 1, 2, 3, 5, 8, 13, ...
        """
        # fibonacci = [0, 1, 1, 2, 3, 5, 8, 13,]

        def get_fibo(n):
            """ return n-th finonacci number """
            if n in (0, 1):
                return n
            return (get_fibo(n - 2) + get_fibo(n - 1))

        fibonacci = []
        for i in range(n):
            fibonacci.append(get_fibo(i))

        return n, fibonacci


    def q06(self, array_str_input):
        """ Q6 숫자의 총합 구하기
        사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을 구하는
        프로그램을 작성하시오. (단 숫자는 콤마로 구분하여 입력한다.)

        input_str = 65,45,2,3,45,8
        """
        array_str = array_str_input.split(',')
        array_int = [int(item) for item in array_str]

        total = 0
        for i in array_int:
            total += i

        return array_int, total


    def q07(self, number_str):
        """ Q7 한 줄 구구단
        사용자로부터 2~9의 숫자 중 하나를 입력받아 해당 숫자의 구구단을 한 줄로 출력
        실행 예) 구구단을 출력할 숫자를 입력하세요(2~9): 2
        2 4 6 8 10 12 14 16 18
        """
        # number_str = input('구구단을 출력할 숫자를 입력하세요(2~9): ')
        # 해도 됨, 입력 귀찮아서 함수의 인자로 처리 함
        return [i * int(number_str) for i in range(1, 10)]


    def q08(self, file_with_dir):
        """ Q8 역순 저장
        다음과 같은 내용의 파일 q08_abc.txt가 있다.
        AAA  -->  EEE
        BBB  -->  DDD
        CCC  -->  CCC
        DDD  -->  BBB
        EEE  -->  AAA
        """
        with open(file=file_with_dir, mode='r', encoding='utf8') as f:
            a_txt = f.read()

        array_a_txt = a_txt.split('\n')
        array_reversed = [array_a_txt[i]
                          for i in range(len(array_a_txt) - 1, -1, -1)]

        # array_reversed = array_a_txt.reverse()   # return None
        return array_a_txt, array_reversed


    def q09(self, keys):
        """ Q9 평균값 구하기
        다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다.
        q09_01_sample.txt 파일의 숫자를 모두 읽어 총합,평균을 구한 후 평균을
        q09_02_result.txt 파일에 쓰는 프로그램을 작성 하시오.
        """
        import numpy as np
        from assets.calc_class import IoReadWrite as io

        (sample_with_dir, result_with_dir) = keys
        sample_txt = io.read_assign(sample_with_dir)

        array_sample_txt = sample_txt.split('\n')
        array_sample_int = [int(item)
                            for item in array_sample_txt
                            if item is not '']
        np_array = np.array(array_sample_int)

        total = np.sum(a=np_array, axis=0)                      # int
        average = np.around(np.average(np_array), decimals=2,)  # float
        num_person = len(np_array)                              # int

        bundle_str = f'{total}/{num_person} = {average:}'
        io.write_to_file(result_with_dir, bundle_str)

        return np_array, total, num_person, average


    def q10(self):
        """ Q10 사칙연산 계산기 -클래스 Calculator를 작성하시오.
        >>> cal1 = Calculator([1,2,3,4,5])
        >>> cal1.sum() # 합계 15
        >>> cal1.avg() # 평균 3.0

        >>> cal2 = Calculator([6,7,8,9,10])
        >>> cal2.sum() # 합계 40
        >>> cal2.avg() # 평균 8.0
        """
        from assets.calc_class import Calculator

        cal1 = Calculator([1, 2, 3, 4, 5])
        print(f"array_i = {cal1.array_int}")    # 합계 15
        print(f"summary = {cal1.sum()}")        # 합계 15
        print(f"average = {cal1.avg()}\n")      # 평균 3.0

        cal2 = Calculator([6, 7, 8, 9, 10])
        print(f"array_i = {cal2.array_int}")    # 합계 15
        print(f"summary = {cal2.sum()}")        # 합계 40
        print(f"average = {cal2.avg()}\n")      # 평균 8.0

        position_import = cal1.__class__        # 'assets.calc_class.Calculator'
        name_class = cal1.__class__.__name__    # Calculator
        funcs_class = [item
                       for item in list(cal1.__class__.__dict__.keys())
                       if not item.startswith("__")
                       ]                                   # ['sum', 'avg']

        return position_import, funcs_class


    def q11(self):
        """Q11. 모듈 사용 방법
        .assets 디렉터리에 mymod.py 파이썬 모듈이 있다고 가정해 보자.
        명령 프롬프트 창에서 파이썬 셸을 열어 이 모듈을 import해서 사용할 수
        있는 방법을 모두 기술하시오.
        (즉 다음과 같이 import mymod를 수행할 때 오류가 없어야 한다.)

        >>> import mymod
        """
        import assets.mymod
        from assets import mymod

        return True


    def q12(self):
        """ Q12 오류와 예외 처리
        다음 코드의 실행 결과를 예측하고 그 이유에 대해 설명하시오.
        >>> result = 0
        >>> item_01 = [1,2,3][3]       # IndexError:
        >>> item_02 = "a" + 1          # TypeError:
        >>> item_03 = 4 / 0            # ZeroDivisionError:

        try:
            code:
        except TypeError:           result += 1
        except ZeroDivisionError:   result += 2
        except IndexError:          result += 3
        finally:                    result += 4
        """
        result = 0

        try:
            array = [1, 2, 3]
            item_01 = array[3]      # IndexError: list index out of range
            item_02 = "a" + 1       # TypeError: must be str, not int
            item_03 = 4 / 0         # ZeroDivisionError: division by zero

        except TypeError:
            result += 1

        except ZeroDivisionError:
            result += 2

        except IndexError:          # 코드 실행순서로, 먼저 에러발생    ... (1)
            result += 3

        finally:
            result += 4             # 조건과 상관없이 끝날 때 항상 실행 ... (2)

        return result


    def q13(self):
        """ Q13 DashInsert 함수
        DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서
        홀수가 연속되면 두 수 사이에 - 를 추가하고, 짝수가 연속되면 * 를
        추가하는 기능을 갖고 있다. DashInsert 함수를 완성 하시오.
        입력 예시: 4546793
        출력 예시: 454*67-9-3
        """
        pass

    def q14():
        """Q14 문자열 압축하기
        문자열을 입력받아 같은 문자가 연속 반복되는 경우에 그 반복 횟수를
        표시해 문자열을 압축하여 표시하시오.
        >>>입력: aaabbcccccca
        >>>출력: a3b2c6a1
        """
        pass

    def q15():
        """Q15 Duplicate Numbers
        0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를
        각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.
        >>>입력: 0123456789 01234 01234567890 6789012345 012322456789
        >>>출력: true false false true false
        """
        pass

    def q16():
        """Q16 모스 부호 해독
        문자열 형식으로 입력받은 모스 부호(dot:. dash:-)를 해독하여 영어
        문장으로 출력하는 프로그램을 작성하시오.
        글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.
        예를 들어 다음 모스 부호는 "HE SLEEPS EARLY"로 해석해야 한다.
        """
        pass

    def q17():
        """Q17 기초 메타 문자
        다음 중 정규식 a[.]{3,}b과 매치되는 문자열은 무엇일까?
        acccb
        a....b
        aaab
        a.cccb
        """
        pass

    def q18():
        """Q18 문자열 검색
        다음 코드의 결괏값은 무엇일까?
        >>> import re
        >>> p = re.compile("[a-z]+")
        >>> m = p.search("5 python")
        >>> m.start() + m.end()
        """
        pass

    def q19():
        """Q19 그루핑
        다음과 같은 문자열에서 휴대폰 번호 뒷자리인 숫자 4개를 ####로 바꾸는
        프로그램을 정규식을 사용하여 작성하시오.
        >>> park 010-9999-9988
        >>> kim 010-9909-7789
        >>> lee 010-8789-7768
        """
        pass

    def q20():
        """Q20 전방 탐색
        다음은 이메일 주소를 나타내는 정규식이다 ---> .*[@].*[.].*$
        이 정규식은 park@naver.com, kim@daum.net, lee@myhome.co.kr 등과 매치
        긍정형 전방 탐 기법을 사용하여 .com, .net이 아닌 이메일 주소는 제외
        시키는 정규식을 작성하시오.
        """
        pass

def get_question_only():
    test = ExamFinal()
    _keys = test.__class__.__dict__.keys()
    def_questions = [item
                    for item in _keys
                    if not item.startswith('__')]   # q1, q2 ....
    func_dict = test.__class__.__dict__
    array_func = [func_dict[key_str] for key_str in def_questions ]
    return [func.__doc__ for func in array_func]

def answer(func, key=None):
    if key:
        [print(item, flush=True) for item in [func.__doc__, func(key)]]
    else:
        [print(item, flush=True) for item in [func.__doc__, func()]]


if __name__ == '__main__':
    import assets._script_run_utf8 as script      # 스트립트런 한글문제 해결
    from os.path import join, dirname

    script.main()
    current_dir = dirname(__file__)
    file_with_dir = join(current_dir, 'static_data', 'q08_abc.txt')
    sample_with_dir = join(current_dir, 'static_data', 'q09_01_sample.txt')
    result_with_dir = join(current_dir, 'static_data', 'q09_02_result.txt')

    questions = get_question_only()
    [print(que) for que in questions]

    test = ExamFinal()

    # answer(test.q01)
    # answer(test.q02, key='C')
    # answer(test.q03)
    # answer(test.q04)
    # answer(test.q05, key=15)
    # answer(test.q06, key='1,2,3,4,5')
    # answer(test.q07, key=2)
    # answer(test.q08, key=file_with_dir)
    # answer(test.q09, key=(sample_with_dir, result_with_dir))
    # answer(test.q10)
    # answer(test.q11)
    # answer(test.q12)

    pass
