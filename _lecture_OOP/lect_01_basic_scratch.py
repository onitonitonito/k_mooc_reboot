""" 클래스 오브젝트 : (객체 지향 프로그래밍 - OOP: Obj. Oriented Progmng)
   ** 함수형 프로그래밍 / 객체지향 프로그래밍 = 파이썬 특징의 2축!

  1.클래스명 작명 = 파스칼 케이스 (ThisIsPascalCase)
  - 클래스 함수(매서드)의 첫번째 인자 = 인스턴스 자신(Self)
  - 클래스간 띄어쓰기는 2칸 / 함수(매서드)는 1칸 이다.

  2.오브젝트(객체) : 클래스 오브젝트 <--> 인스턴스
  - 값 (field) = 클래스변수 or 인스턴스 변수
  - 기능 (method) = 매서드, 매직매서드, 더블언더스코어

  3.클래스만의 매우 특별한 기능
   * 상속 (Inherit) = 부모(Parent) - 자식(Child)
   * 중복 (Override) = 덮어쓰기 / 겹쳐쓰기
 """
import _script_run_utf8
_script_run_utf8.main()


class ManOne(object):
    icon = '성격 나쁨'

    def __init__(self, name):
        self.name = name
        self.__my_secret = '말할 수 없는 비밀!'

    def say_hello(self, other_obj):
        print("{}: 안뇨옹~!! '{}'!".format(self.name, other_obj.name))

    def __del__(self):
        print("{} 죽다..".format(self.name))

    def __add__(self, other_obj):
        print("{}, {}.. 행복하게 결혼하다.".format(self.name, other_obj.name))

    def __sub__(self, other_obj):
        print("{}, {}.. 결국 이혼하다.".format(self.name, other_obj.name))

    """ 클래스 매서드는, 인스턴스 명으로 클래스변수에 접근할 방법을 열어준다."""
    @classmethod
    def set_icon_change(cls, modified_string):
        cls.icon = modified_string

    """ 스테틱 매서드는, 객체기능과 상관없지만 그림(편의)상 포함시켜야 할 때"""
    @staticmethod
    def show_shortened_life_story_with(obj1, obj2):  # 상관없으니 'self'인자 없음
        print("\n\n'{}'와 '{}'의 짧은 인생스토리~ 시작!!.."
              '\n--------------------'.format(obj1.name, obj2.name))
        obj1 + obj2
        obj1 - obj2
        obj1.__del__()
        print('\n\n')

    # '프라이빗' 매서드는 인스턴스로 보이지 않는다. = 클래스로 호출한다.
    def __dont_use_by_anyone(self):
        print("*** 어떤! '인스턴스'도 /접/근/금/지/..!! ***")


class ManTwo(ManOne):
    icon = '성격 좋음'

    def say_thank_you(self, other_obj):
        print("{}: 고마우어이~~ '{}!'".format(self.name, other_obj.name))


m1, m2 = ManOne('철수'), ManTwo('영희')         # 객체 선언! .. 뾰로롱~!!

m1.say_hello(m2)
m2.say_thank_you(m1)
# m1.say_thank_you(m2)      # 에러: 맨1은 땡큐기능 없음! = 성격 더럽기 때문

""" 여기서,  질문~!!:
.. 성격을 알아보는 기능은 어느 객체의 것일까? = 공통기능 (바깥에 정의)
   (또는 스테틱 매서드로, 그냥 그림(편의)상 포함만 시켜 놓을 수 있다.)
"""
def show_secret_of(obj):
    print("{}의 성격은... {}".format(obj.name, obj.icon))


show_secret_of(m1)
show_secret_of(m2)

""" 클래스변수에 접근하는 방법은 2가지
  - 클래스명으로 직접 접근하는 방법
  - 클래스 매서드로, 인스턴스로도 접근 가능(!)
"""
# ManTwo.icon = '성격이 매우 더러움'
m2.set_icon_change(modified_string='성격이 매우더러움')

m2.icon = '성격이 매우 더러움'
show_secret_of(m2)

m22 = ManTwo('똘똘이')
show_secret_of(m22)


# @staticmethod (스태틱매서드)를 호출할 때는, 객체 상관없지만, '인스턴스'로 호출!! """
m1.show_shortened_life_story_with(m1, m2)

""" 프라이빗 매서드(더블언더스코어)를 호출하는 방법
  - 파이썬은 기본적으로 '퍼블릭'이다... 가정: 양식이 있는, 다 큰 어른이 뭘 숨기나?
  - '더블언더스코어'는 '맹글링' 목적도 있다. (동일이름의 중복 매서드 구분)
    # 'ManOne' object has no attribute '__dont_use_by_anyone'
    # m1.__dont_use_by_anyone()        # 안된다...!!
    # ManOne.__dont_use_by_anyone()    # 안된다니까... ?!!
"""
m1._ManOne__dont_use_by_anyone()
print(m1._ManOne__my_secret)
