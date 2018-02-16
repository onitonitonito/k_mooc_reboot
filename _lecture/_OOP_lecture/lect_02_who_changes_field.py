import _script_run_utf8
_script_run_utf8.main()

def _01_클래스변수와_매서드변수의_변경권한():
    """ 주체 = 오브젝트냐? 인스턴스냐?
    """
    class TestClass(object):     # 클래스명은 파스칼 타입 = 기본 '오브젝트'를 상속한다.
        class_string = '클래스변수 - 원본: 실험적 테스트 스트링'

        def __init__(self):
            self.method_string = '매서드변수 - 원본: 우발적 테스트 스트링\n'


    tc = TestClass()
    print(tc.class_string)   # 클래스변수 - 실험적 테스트 스트링
    print(tc.method_string)  # 매서드변수 - 우발적 테스트 스트링
    TestClass.class_string = '클래스변수 - **변경: TestClass 가 실험적 고침'
    TestClass.method_string = '매서드변서 - **변경: TestClass 가 우발적 고침\n'

    print(tc.class_string)   # 클래스변수 - 실험적 테스트 스트링
    print(tc.method_string)  # 매서드변수 - 우발적 테스트 스트링

    print('--------------- 비교해봅시다 tc vs. ac --- \n')
    ac = TestClass()
    print(ac.class_string)   # 클래스변수 - 실험적 테스트 스트링
    print(ac.method_string)  # 매서드변수 - 우발적 테스트 스트링
    ac.class_string = '클래스변수 - **변경: ac 가 실험적 고침'
    ac.method_string = '매서드변서 - **변경: ac 가 우발적 고침\n'

    print(ac.class_string)   # 클래스변수 - 실험적 테스트 스트링
    print(ac.method_string)  # 매서드변수 - 우발적 테스트 스트링
# _01_클래스변수와_매서드변수의_변경권한()
