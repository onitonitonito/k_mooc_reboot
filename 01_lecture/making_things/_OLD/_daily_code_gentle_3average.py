import os

def read_average():
    print("3개의 0~100 사이의 숫자를 [space]로 구분해서 입력하시오 :")
    values = input().split()

    while True:
        try:
            f1 = [float(value) for value in values] # 3 float() lists
            break
        except ValueError:
            print("Type error, Try in float type..")
            raise


    for value in values:
        if float(value) == False:
            return "There's an error. Try agrain.."

    float_numbers = [float(value) for value in values]
    for float_n in float_numbers:
        if float_n > 0 and float_n < 100:
            [n1, n2, n3] = float_numbers
            average = (n1 + n2 + n3) / 3
            return "The average is {:.2f}".format(average)
        else:
            return "The values is out of range( 0< value <100)"

def run_average_3floats():
    """
    # (1) 입력 값에 대한 에러처리(예외처리) 문제 - raise 언제?
    # (2) 루프문에 대한 탈출문제 - pass, continue, break 언제?
    """
    print(INSTRUCTOIN_NOTICES[0])
    while True:
        """ 입력에러 체크 """
        try:
            str_numbers = input(INSTRUCTOIN_NOTICES[1]).split()
            float_numbers = [float(number) for number in str_numbers]

            """ 입력항의 갯수, 3개인가 체크"""
            if len(float_numbers) != 3:
                print(ERROR_CODES[1] + "\n\n\n")
                continue

            """ 입력값이 범위를 벗어났는지 체크 (0 < x < 100) """
            if False in [ 0 < float_n < 100 for float_n in float_numbers]:
                print(ERROR_CODES[2] + "\n\n\n")
                continue

        except ValueError:
            print(ERROR_CODES[3] + "\n\n\n")
            continue

        """ 입력 값에 문제없음 --> 계산결과 실행 """
        average = sum(float_numbers)/len(float_numbers)
        print("{1:}개 숫자의 평균값은 {2:.3f} 입니다.. \n\n\n\n".format(
            len(float_numbers),
            average))

        if input("그만할까요?(Y/N=Enter)").lower().startswith("y"):
            break

        os.system('cls')


INSTRUCTOIN_NOTICES = [
    "=== 3개 숫자 평균내는 프로그램 ===\n" +\
    " 1) 3개의 숫자 (실수,정수)를 입력 받음\n" +\
    " 2) 3개의 숫자를 평균내 줌\n" +\
    "   *미션.1: 의도하지 않은 Terminated를 방지할 것\n" +\
    "   *미션.2: CASE별 에러메시지로 양질의 입력값을 받을 것\n" +\
    "================================\n",

    "안내문: 0~100 사이 3개숫자 [space]구분, 입력하시오 : "]
ERROR_CODES = [
    "_0=버림_^^_",
    "[Error.01] ... 정확히 3개의 숫자를 입력 해 주세요",
    "[Error.02] ... 입력 숫자가 범위(0 < x < 100)를 벗어났습니다",
    "[Error.03] ... 입력한 숫자(float)가 아닙니다."]

if __name__ == '__main__':
    """ 최초의 제안 """
    read_average()

    """ 리펙토링 & 완성 """
    # run_average_3floats()
