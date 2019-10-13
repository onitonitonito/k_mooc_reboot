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
class ManOne(object):
    icon = '성격이 나쁨'

    def __init__(self, name, age):
        """ 생성자: 객체가 생성되면 제일 먼저 실행되는 매서드 """
        self.name = name
        self.age = age

    def say_hello(self, other_instance):
        print('{}({}세): 안녕하세요~  {}({}세)씨...'.format(
            self.name,
            self.age,
            other_instance.name,
            other_instance.age,
            ))

    def __add__(self, other_instance):
        print("{}와 {}가 결혼하다... ".format(self.name, other_instance.name))

    def __sub__(self, other_instance):
        print("{}와 {}가 결국은 이혼하다...".format(self.name, other_instance.name))

    def __del__(self):
        print("{}.. 외롭게 죽다...".format(self.name))

    def show_shortened_life_story_with(self, other_instance):
        """ '매직 메서드'를 조합한 기능 """
        print("------------------------\n"
            "{}, {}의 인생스토리: 서사시\n"
            "------------------------".format(self.name, other_instance.name))
        # m10.__add__(m20)
        self + other_instance
        # m10.__sub__(m20)
        self - other_instance
        # m10.__del__()
        # del(self)
        self.__del__()

    """ 여기서,  질문~!!:
    .. 성격을 알아보는 기능은 어느 객체의 것일까? = 공통기능 (바깥에 정의)
       (또는 스테틱 매서드로, 그냥 그림(편의)상 포함만 시켜 놓을 수 있다.)
       '@' = 장식자 : 데코레이터
    """
    @staticmethod
    def show_secret_of(obj):
        print("'{}'의 성격은... {}".format(obj.name, obj.icon))

    """ 클래스 매서드는, 인스턴스 명으로 클래스변수에 접근할 방법을 열어준다."""
    @classmethod
    def set_icon_change(cls, modified_string):
        cls.icon = modified_string

    """ 스테틱 매서드는, 객체기능과 상관없지만 그림(편의)상 포함시켜야 할 때"""
    @staticmethod
    def show_life_story_with(obj1, obj2):  # 상관없으니 'self'인자 없음
        print("\n\n'{}'와 '{}'의 짧은 인생스토리~ 시작!!.."
              '\n--------------------'.format(obj1.name, obj2.name))
        obj1 + obj2
        obj1 - obj2
        obj1.__del__()
        print('\n\n')

class ManTwo(ManOne):
    icon = '성격이 좋음'    # 오버라이드 (덮어쓰기)

    def say_thank_you(self, other_instance):
        print("{}({}세): 고마우어이~~ '{}'!".format(
            self.name,
            self.age,
            other_instance.name,
            ))

""" 객체 선언(생성) : m10, m20=인스턴스 <--> 오브젝트 = 클래스 객체 """

m10 = ManOne('철수', 24)
m11 = ManOne('똘이', 11)
m12 = ManOne('맹구', 15)

m20 = ManTwo('영희', 17)

m10.say_hello(m20)
m20.say_hello(m10)
m20.say_thank_you(m10)
# m10.say_thank_you(m20)   # 부모는 자식'매서드'를 물려받을수 없다.


# m10.icon = '성격이 아주아주 더러움'
ManOne.icon = '성격이 아주아주 더러움'

m10.say_hello(m20)

# show_secret_of(m10)
# show_secret_of(m11)
# show_secret_of(m12)

for instance in [m10, m11, m12]:
    instance.show_secret_of(instance)

""" 철수와 영희의 인생 대서사시 : 기능 """
# m10.show_shortened_life_story_with(m20)
m10.show_life_story_with(m10, m20)
