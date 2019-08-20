"""
# 각종 변수를 저장하기 위한 config asset
#
"""
# print(__doc__)

from os.path import join, dirname

current_dir = dirname(__file__)

file_with_dir = join(current_dir, 'static_data', 'q08_abc.txt')
sample_with_dir = join(current_dir, 'static_data', 'q09_01_sample.txt')
result_with_dir = join(current_dir, 'static_data', 'q09_02_result.txt')

array_number_str_space = '0123456789 01234 01234567890 6789012345 012322456789'

array_re_target = [
                    'acccb',
                    'a....b',
                    'aaab',
                    'a.cccb',
                ]

name_phone_str_space = 'park 010-9999-9988 kim 010-9909-7789 lee 010-8789-7768'
