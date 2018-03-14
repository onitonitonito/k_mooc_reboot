""" 클래스 객체/오브젝트 : (객체 지향 프로그래밍 - OOP: Obj. Oriented Progmng)
#  ** 함수형 프로그래밍 / 객체지향 프로그래밍 = 파이썬 특징의 2축!
#  : 클래스 객체 = 흔히 붕어빵 틀(클래스) <--> 붕어빵(인스턴스)에 비유한다.
#  :   붕어빵 틀은 1개 인데, 팥-붕어빵, 크림-붕어빵, 다양한 변종을 찍어낸다.
#  :   찍어 낸 (인스턴스)는 독립적으로 작동 한다(self)
#
# 1.클래스명 작명 = 파스칼 케이스 (ThisIsPascalCase)
# - 클래스 함수(매서드)의 첫번째 인자 = 인스턴스 자신(Self)
# - 클래스간 띄어쓰기는 2칸 / 함수(매서드)는 1칸 이다.
#
# 2.오브젝트(객체)의 특징! : 클래스 오브젝트 <--> 인스턴스
# - (1) 값 (field) = 클래스변수 or 인스턴스 변수
# - (2) 기능 (method) = 매서드, 매직매서드, 더블언더스코어
#
# 3.클래스만의 매우 특별한 기능
#  * 상속 (Inherit) = 부모(Parent) - 자식(Child)
#  * 중복 (Override) = 덮어쓰기 / 겹쳐쓰기
"""
# import _script_run_utf8
# _script_run_utf8.main()

class FishBread(object):
    """ 속없는 붕어빵 """
    counter = 0

    def __init__(self):
        self.ingredient = ['Flour', 'Water']
        self.name = 'Brave-FishBread'


class ReadBeanFishBread(FishBread):
    """ 단팥 붕어빵 """
    def __init__(self):
        super().__init__()
        FishBread.counter += 1
        self.name = 'Brave-ReadBeanFishBread'
        self.ingredient.append('ReadBean')


class CreamFishBread(FishBread):
    """ 크림 붕어빵 """
    def __init__(self):
        super().__init__()
        FishBread.counter += 1
        self.name = 'Brave-CreamFishBread'
        self.ingredient.append('Cream')


class ReadBeanCreamFishBread(ReadBeanFishBread, CreamFishBread):
    """ 단팥 크림 붕어빵 = 단팥맛 + 크림맛 (다 중상속) / 2번 카운트 보정
     - '상속'은 2단계 이상 내려가지 말 것 .... '혼돈'에 빠진다
     - '다이아몬드' 상속이 발생 하면, 각별히 '상속' 순서/병합에 주의할 것!!
    """
    def __init__(self):
        super().__init__()
        FishBread.counter -= 1      # 카운터를 2번 올리므로, 1번은 빼준다.
        self.name = 'ReadBeanCreamFishBread'


class ReadBeanCreamChocoFishBread(ReadBeanCreamFishBread):
    """ 단팥 크림 초코 붕어빵 = 단팥/크림(상속) + 초코 (상속 후 재료만 추가)"""
    def __init__(self):
        super().__init__()
        self.name = 'ReadBeanCreamChocoFishBread'
        self.ingredient.append('Choco')




# bf1 = FishBread()                       # '용감한 붕어빵'은 세지 않는다.
# print(bf1.name, '=', bf1.counter)

rf1 = ReadBeanFishBread()
print(rf1.name, '=', rf1.counter, rf1.ingredient)

cf1 = CreamFishBread()
print(cf1.name, '=', cf1.counter, cf1.ingredient)

rcf1 = ReadBeanCreamFishBread()
print(rcf1.name, '=', rcf1.counter, rcf1.ingredient)

rccf1 = ReadBeanCreamChocoFishBread()
print(rccf1.name, '=', rccf1.counter, rccf1.ingredient)

_="""*** 4 단계, 상속의 'MRO(Method Resolution Order)'를 찍어보자..
  - mro를 통해서 '상속'의 우선순위를 확인 할 수 있다.
-------------------------------------------------"""
print('\n\n'+_)
for i, mro in enumerate(rccf1.__class__.__mro__,1):
    print("%s. %s"%(i, mro))




_="""*** 인구(인스턴스)를 늘려 가며, 통계(클래스변수)를 확인해 보자 """
print('\n\n\n'+_)
def basic_test():
    class Human(object):
        popularity = 0
        name_dict = dict()

        def __init__(self, name):
            self.name = name
            self.cloth = 1

            Human.popularity += 1
            Human.name_dict[Human.popularity] = [
                name,
                self.__class__.__name__,
                self.__class__,
                ]

        def say_hello(self, other_obj):
            print("'{}'({})에게...".format(
                other_obj.name,
                other_obj.__class__.__name__
            ))
            print("안녕하십니까? 제 이름은 '{}'({})입니다...".format(
                self.name,
                self.__class__.__name__,
            ))

        @classmethod
        def show_status(cls):
            print('\n현재 인구수 : %s 명'% cls.popularity)
            print('-----------------------------')
            for key in cls.name_dict:
                print("{:2}....'{:6}'({:})".format(
                    key,
                    cls.name_dict[key][0],
                    cls.name_dict[key][1],
                     ))
            print('-----------------------------\n\n')


    class Male(Human):

        def __init__(self, name):
            super().__init__(name)
            self.shield = 1

        def __str__(self):
            return "'%s' -- class Male Human" % self.name


    class Female(Human):

        def __init__(self, name):
            super().__init__(name)
            self.weapon = 1




    if __name__ == '__main__':
        # 인구를 2명 추가해 봅니다.
        ma = Male('Chris')
        fe = Female('Alisa')

        # 현재의 상태를 봅시다.. '클래스 메서드'
        # Human.show_status()   # ... 이건, '파2'방법이라고 한다, 놔주자!
        # classmethod(Human.show_status())
        # classmethod(ma.show_status())       # 어디서든 접근가능!
        classmethod(fe.show_status())       # 어디서든 접근가능!

        ma.say_hello(fe)

        # 인구를 6명 더 추가 해 봅니다.
        inst_dict = {'ma' + str(i + 1): name
                     for i, name in enumerate(
                     ['Park', 'Lee', 'Choi', 'Kim', 'Jun', 'Jung'])}
        for key in inst_dict:
            key = Male(inst_dict[key])

        # classmethod(Human.show_status())
        # classmethod(ma.show_status())       # 어디서든 접근가능!
        classmethod(fe.show_status())       # 어디서든 접근가능!
basic_test()
