import os

TEMP_FORMAT_01 ='''
=================================================
  This program convert celcious degree to
  Fahrenheit degree temperature.
  Input c.degree which want to be converted
-------------------------------------------------
  INPUT TEMP : '''

TEMP_FORMAT_02 = '''
 * Dom. Eg : F.degree = ((9/5) * c.degree ) + 32

      (1) Celcious.D   : %s dC
      (2) Fahrenheit.D : %.2f dF
_________________________________________________'''

os.system('cls')

input_degree = float(input(TEMP_FORMAT_01))
fahr_degree = ( (9/5) * input_degree ) + 32

print(TEMP_FORMAT_02 % (input_degree, fahr_degree))
