""" '클래스' / '인스턴스' 변수 - 누가 '접근권한'있나? / 어떻게 바뀌나? """
# - 클래스 변수를, 클래스로 접근하여 바꾼다 = '붕어빵 틀'을 바꿔버림
# - 인스턴스 변수를, 인스턴스로 접근해서 바꾼다 = '개인 성격'만 바꿈.

import _script_run_utf8
_script_run_utf8.main()


class TestClass(object):     # 클래스명은 파스칼 타입 = 기본 '오브젝트'를 상속한다.
    class_string = '클래스변수 - 원본: 실험적 테스트 스트링'

    def __init__(self):
        self.method_string = '매서드변수 - 원본: 우발적 테스트 스트링\n'


ac = TestClass()
# 1. '인스턴스'가 변경하는 경우
print(ac.class_string)   # 클래스변수 - 원본: 실험적 테스트 스트링
print(ac.method_string)  # 매서드변수 - 원본: 우발적 테스트 스트링
ac.class_string = '클래스변수 - **변경: ac 가 실험적 고침'
ac.method_string = '매서드변서 - **변경: ac 가 우발적 고침\n'

print(ac.class_string)   # 클래스변수 - **변경: ac 가 실험적 고침
print(ac.method_string)  # 매서드변서 - **변경: ac 가 우발적 고침

oac = TestClass()
print(oac.class_string)   # 클래스변수 - 원본: 실험적 테스트 스트링
print(oac.method_string)  # 매서드변수 - 원본: 우발적 테스트 스트링

print('--------------- 비교해봅시다 tc vs. ac --- \n')

tc = TestClass()
# 2. '클래스 객체'가 변경하는 경우
print(tc.class_string)   # 클래스변수 - 원본: 실험적 테스트 스트링
print(tc.method_string)  # 매서드변수 - 원본: 우발적 테스트 스트링
TestClass.class_string = '클래스변수 - **변경: TestClass 가 실험적 고침'
TestClass.method_string = '매서드변서 - **변경: TestClass 가 우발적 고침\n'

print(tc.class_string)   # 클래스변수 - **변경: TestClass 가 실험적 고침
print(tc.method_string)  # 매서드변수 - 원본: 우발적 테스트 스트링

otc = TestClass()
print(otc.class_string)   # 클래스변수 - **변경: TestClass 가 실험적 고침
print(otc.method_string)  # 매서드변수 - 원본: 우발적 테스트 스트링


# 실행 결과
"""
클래스변수 - 원본: 실험적 테스트 스트링
매서드변수 - 원본: 우발적 테스트 스트링

클래스변수 - **변경: ac 가 실험적 고침
매서드변서 - **변경: ac 가 우발적 고침
"""
# .... 결론 : 원본(붕어빵 틀)에는 변함이 없다
"""
클래스변수 - 원본: 실험적 테스트 스트링
매서드변수 - 원본: 우발적 테스트 스트링

--------------- 비교해봅시다 tc vs. ac ---

클래스변수 - 원본: 실험적 테스트 스트링
매서드변수 - 원본: 우발적 테스트 스트링

클래스변수 - **변경: TestClass 가 실험적 고침
매서드변수 - 원본: 우발적 테스트 스트링
"""

# .... 결론1 : '클래스 객체'가 접근하면 원본(붕어빵 틀)을 변형시킴.
# .... 결론2 : 하지만, '매서드 변수'에는 접근권한이 없음..
"""
클래스변수 - **변경: TestClass 가 실험적 고침
매서드변수 - 원본: 우발적 테스트 스트링
"""
