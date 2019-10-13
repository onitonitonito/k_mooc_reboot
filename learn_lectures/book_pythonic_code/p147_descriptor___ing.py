"""
# BETTER WAY31 - Let's Use Descriptor on the reusable @property method
"""
# BETTER WAY31 - 재사용 가능한 @property 메서드에는 디스크립터를 사용하자


class Grade(object):
    """점수를 기록하기 위한 점수 클래스"""
    def __init__(self):
        """오브젝트 생성시, 점수를 '0'으로 초기세팅 한다."""
        self._value = 0

    def __get__(self, instance, instance_type):
        return self._value

    def __set__(self, instance, value):
        """점수 입력(오브젝트 생성)시 0~100 범위의 값만 받는다."""
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100!')
        self._value = value


class Exam(object):
    """
    # 과목별 오브젝트, 초기값을 선언하는 클래스
    """
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


def main():
    """ 중간고사를 선언해 준다고 했으면 """
    mid_term = Exam()

    # Setter option ... 선언방식은 다르지만 같은셋팅이다.
    mid_term.math_grade = 40
    Exam.__dict__['writing_grade'].__set__(mid_term, 60)  # the same way
    Exam.__dict__['science_grade'].__set__(mid_term, 80)  # the same way

    # Getter option ... 가저오는 방식은 다르지만 결과는 같다.
    _math_getter = mid_term.math_grade
    _writing_getter = Exam.__dict__['writing_grade'].__get__(mid_term, Exam)  # the same way
    _science_getter = Exam.__dict__['science_grade'].__get__(mid_term, Exam)  # the same way

    # Getter 의 결과를 확인해 보면 같다.
    print(_math_getter)           # 40
    print(_writing_getter)        # 60
    print(_science_getter)        # 80



if __name__ == '__main__':
    main()
