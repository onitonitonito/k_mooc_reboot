"""
# 문자열을 효율적으로 concat 하는 방법 https://118k.tistory.com/447
# 파이썬에서 문자열을 효율적으로 concat 방법 찾다가 좋은 사이트 발견
  - 방법6이 가장 효율적인 방법이나,
  - 메모리 사용량은 방법4가 가장 효율적이고,
  - 문자열에 조작을 해야 하는 경우라면 방법4가 가장 효율적이다.
"""
# 원문에서 방법 4, 5, 6을 추천.
# 방법 6이 가장 빠르기 때문에 많이 사용
# 방법 4는 처리시 문자열 변환하려고 할 때 유연하게 적용 가능.
# 방법 5는 가상파일 이용하기 때문에 메모리 사용량 가장 효율적.
# 방법 4, 6 리스트를 이용하기 때문에 문자열 많아지면 메모리 사용량 늘어남.

def main():
    # print(run_01())
    # print(run_02())     # DEPRECATED : UserString은 더이상 지원않는 클래스
    print(run_03())
    # print(run_04())
    # print(run_05())      # DEPRECATED : cStringIO은 더이상 지원않는 클래스
    # print(run_06())
    pass


def run_01():
    """# 방법1: + 를 이용한 연결"""
    out_str = ''
    for num in range(10):
        out_str += 'num--'
    return out_str

def run_02():
    """# 방법2: MutableString 이용한 방법
    - DEPRECATED : UserString은 더이상 지원않는 클래스
    """
    from UserString import MutableString
    out_str = MutableString()
    for num in range(10):
        out_str += 'num--'
    return out_str

def run_03():
    """# 방법3: 캐릭터 배열을 이용한 방법 - """
    from array import array
    char_array = array('b')

    for num in range(10):
    #     char_array.fromstring('num--') # fromstring is DEPRECATED
    # return char_array.tostring()

        char_array.frombytes(b'num--')
    return char_array.tobytes()


def run_04():
    """# 방법4: 리스트의 join()을 이용한 방법"""
    str_list = []
    for num in range(10):
        str_list.append('num--')
    return ''.join(str_list)

def run_05():
    """# 방법5: 수도 파일을 이용하는 방법"""
    from cStringIO import StringIO
    file_str = StringIO()
    for num in range(10):
        file_str.write('num--')
    return file_str.getvalue()

def run_06():
    """# 방법6: 방법4와 복합 리스트를 이용한 방법"""
    return ''.join(['num--' for num in range(10)])





if __name__ == "__main__":
    main()
