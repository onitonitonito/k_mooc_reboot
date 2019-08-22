"""
# 각종 변수를 저장하기 위한 config asset
#
"""
# print(__doc__)

from os.path import join, dirname

current_dir = dirname(dirname(__file__))      # 현재보다 상위 = dir(dir(현재))

file_with_dir = join(current_dir, 'static_data', 'q08_abc.txt')
sample_with_dir = join(current_dir, 'static_data', 'q09_01_sample.txt')
result_with_dir = join(current_dir, 'static_data', 'q09_02_result.txt')

array_number_str_space = '0123456789 01234 01234567890 6789012345 012322456789'
array_re_target = ['acccb', 'a....b', 'aaab', 'a.cccb']
name_phone_str_space = 'park 010-9999-9988 kim 010-9909-7789 lee 010-8789-7768'

# 클래스 실헹 args 조합을 dict로 정의한다.  --> answer() 를 실행
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
# answer(test.q13, key=4546793)
# answer(test.q14, key='aaabbcccccca')
# answer(test.q15, key=array_number_str_space)
# answer(test.q16, key="HE SLEEPS EARLY")
# answer(test.q17, key=array_re_target)
# answer(test.q18)
# answer(test.q19, key=name_phone_str_space)

dict_arg_answer = {
        '01': None,
        '02': 'C',
        '03': None,
        '04': None,
        '05': 15,
        '06': '1,2,3,4,5',
        '07': 2,
        '08': file_with_dir,
        '09': (sample_with_dir, result_with_dir),
        '10': None,
        '11': None,
        '12': None,
        '13': 4546793,
        '14': 'aaabbcccccca',
        '15': array_number_str_space,
        '16': "HE SLEEPS EARLY",
        '17': array_re_target,
        '18': None,
        '19': name_phone_str_space,
        '20': None
    }
