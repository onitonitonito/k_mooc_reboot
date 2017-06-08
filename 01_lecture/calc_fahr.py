import os


TEMP_FORMAT ='''
============================================
본 프로그램은 섭씨를 화씨로 변환시켜 줍니다.
변환 하고 싶은 섭씨 온도를 입력해 주세요
--------------------------------------------
INPUT TEMP : %s

   계산공식 : FAHRENHEIT = ((9/5)* 섭씨온도)+32

(1) 섭씨온도 : %s
(2) 화씨온도 : %.2f
____________________________________________'''

os.system('cls')

input_degree = float(input('섭씨를 입력해 주세요:'))
fahr_degree = ( (9/5) * input_degree ) + 32

print(TEMP_FORMAT % (input_degree, input_degree, fahr_degree))

# print(TEMP_FORMAT %('103.24', '123.02', '2332') )
