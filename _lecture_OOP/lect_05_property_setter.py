""" @프로퍼티 데코레이터 / 프로퍼티를 수정하는 @func.Setter (쌍으로 사용)
@property
def attribute(self):

@attribute.setter
def attribute(self,value):
"""
import _script_run_utf8
_script_run_utf8.main()

""" @프로퍼티 데코레이터를 사용하는 이유(!)
 - 변수처럼 변경이 가능 함: ins1.name = 'Alex'
 - 변수를 변경할때 제약을 둠 / 하위 호환성에 도움이 됨.
 - 따로 get() set() 함수를 만들지 않고 간단히 사용가능.
"""


class Person(object):
    def __init__(self, name):
        self.__name = name       # 'private' = ins._class__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

ps = Person('Alex')
ps.name = 'Lisa'                # set self.__name = 'Lisa'
_= """1. @property / @func.setter 이용 """
print(_)
print("  ps.name = '%s'\n"% ps.name)                  # 'Alex' or 'Lisa'

ps._Person__name = 'Kristen'
_="""2. 인스턴스 변수, 바로 접근이 가능하다(?) """
print(_)
print("  Kristen = %s"% ps._Person__name)         # 'private' 으로도 가능하다.
print("  Kristen = %s\n"% ps.name)                  # 동일하게 호출할 수 도 있다.

ps1 = Person('Michael')
_="""3. 인스턴스 변수는 한 객체에만 영향을 준다 (빵틀은 안 바뀜) """
print(_)
print("  ps = %s"% ps.name)
print("  ps1= %s"% ps1.name)


class SetColor(object):
    def __init__(self):
        self._color = 'red'         # 'protected' or 'private'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, colors):
        self._color = colors



sc = SetColor()
sc.color = 'blue'                 # set self.__color = 'blue'
_="""4. color change by @프로퍼티 @펑션.세터 이용시 """
print('\n'+_)
print("  sc.color = %s"% sc.color)                     # red / blue
print('\n\n')



class Celsius(object):
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return self.get_temperature()*1.8 + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError(" -273도 이하는 불가능 합니다.")
        self._temperature = value



_="""** 1. get() set() 설정: set(), get()통해서 제약(조건)을 둘수 있다 """
print('\n'+_)
c = Celsius()                   # tmperature 초기값 = set()으로 0 설정
c.set_temperature(-11)           # set()으로 30 설정
# c.set_temperature(-300)         # -273 이하는, 강제로 ValueError 발생시킴
# c._temperature = -300           # 직접 접근하면, 제약을 할수 없다 (이럼 안됨)

print("  to celsius = %s 'c'"% c.get_temperature())      # get()으로 30 읽어옴
print("  to fahren  = %s 'f'"% c.to_fahrenheit())        # 화씨로 변경시킴
print("  self._temp = %s"% c._temperature)



class CelsiusChange(object):
    def __init__(self, celsius=0):
        self.__celsius = celsius

    def get_celsius(self):          # get()을 삭제하고, 직접 접근도 됨
        return self.__celsius

    def to_fahrenheit(self):
        return self.get_celsius()*1.8 + 3.2

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        self.__celsius = value



cc = CelsiusChange(0)
cc.celsius = -11

_="""** 2. @프로퍼터, @펑션.세터 를 사용하는 경우 : get(), set() 없이 간단히.. """
print('\n'+_)
print("  to celsius = %s 'c'"% cc.celsius)      # get()으로 30 읽어옴
print("  to fahren  = %s 'f'"% cc.to_fahrenheit())        # 화씨로 변경시킴
print("  ins._Class__private = %s 'c"% cc._CelsiusChange__celsius )
