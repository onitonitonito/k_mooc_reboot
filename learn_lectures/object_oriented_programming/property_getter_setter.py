"""
# How to use - property / getter, setter
#    - practice several getter/setter method
"""
# print(__doc__)


def main():
    # age_getter_setter = property(**age_getter_setter())
    # print(age_getter_setter)      # <property object>
    # print(age_getter_setter.fget) # <function age_getter_setter.<locals>.fget>

    movie_setter_run()
    geeks_for_geeks_run()
    geeks_run()
    sample_class_run()
    fianl_class_run()
    c_run()
    test03_setter()
    pass


def test03_setter():
    from math import sqrt

    class SmartPoint(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        @property
        def hypotenuse(self):
            return sqrt(self.x ** 2 + self.y ** 2)

        @hypotenuse.setter
        def hypotenuse(self, z):
            # Sily setter example .. 값을 정(set)해주면 self.y를 변경
            self.y = sqrt(z ** 2 - self.x ** 2)

    point = SmartPoint(3, 4)
    # Callable 함수는 없다. 속성 값만 있다.
    # print(point.hypotenuse)     # 5.0  ... sqrt(3**2 + 4**2) = sqrt(25)

    point.hypotenuse = 6         # 리턴값(set) = 정해진값(x)를 놔두고 (y역산)

    # 3 5.196152422706632 ... 역산(y) = 5.1961..
    print(f"point.x, point.y = ({point.x}, {point.y})")
    print()

def movie_setter_run():
    # Call class with init variables
    mv = Movie('Super Man')

    # comparison property to direct hidden variiable ... True Super Man
    print(mv.movie_name is mv._Movie__movie_name, mv.movie_name)

    funcs = [func
            for func in mv.__dir__()
            if func.startswith("_")
            ]

    # 변수값을 바꾸는것 같지만, 프로퍼티로 지정된 메서드를 setter 메서드로 변경한다.
    # 사용(접근)하는 방법은 변수와같이 사용한다.
    mv.movie_name = 'Spider Man'
    print("both hidden & variable(property) are changed?:",
            mv.movie_name is mv._Movie__movie_name,
            mv.movie_name)

    # 히든값에 직접 접근해서 바꿀수도 있다 (변칙)
    mv._Movie__movie_name = "JOKER COMES AROUND!"

    mv.movie_name = "Iron Man"
    print("... Touched Secret Variable directly! w/o setter ...")
    print(mv.movie_name == mv._Movie__movie_name, mv.movie_name)

    print(f" - BEFORE: {mv._Movie__before_name}")
    print(f" - AFTER : {mv._Movie__movie_name}")

def geeks_for_geeks_run():
    """ age = property() 실행 전/후 비교"""

    # property() 이 없을 때, 실행 방법
    kay = GeeksForGeeks()
    kay.set_age(21)         # set- setter method called!
    print(kay.get_age())    # 21 - getter method called!
    print(kay._age)         # 21 - for test!
    kay.del_age()           # del- deleter method called!

    # property() 지정 후, 실행 방법 (변수처럼 자연스럽게 사용한다)
    jay = GeeksForGeeks()
    jay.age = 10            # set- setter method called!
    print(jay.age)          # 10 - getter method called!
    print(jay._age)         # 10 - for test!
    del jay.age             # del- deleter method called!
    pass

def geeks_run():
    mark = Geeks()
    mark.age = 19           # set- setter method called!
    print(mark.age)         # 19 - getter method called!

    park = Geeks()
    print(park.age)         # 0 - getter method called!
    park.age = 17           # NG-'Geeks' is not permitted, under age of 18!
    pass

def sample_class_run():
    obj = SampleClass(10)
    print(obj.get_a())    # 10 - getter method called!
    obj.set_a(45)         # set- setter method called!
                          # Not an even number, set a as 2 now!
    print(obj.get_a())    # 2 - getter method called!
    obj.set_a(16)         # Accepted!, set a as '16' now!
    pass

def fianl_class_run():
    """
    _FinalClass__a      ... hidden var.
    _FinalClass__get_a  ... hidden func()
    _FinalClass__set_a  ... hidden func()
    a                   ... set a as property()
    """
    fc1 =FinalClass(10)      # Accepted!, set a as '10' now!
    fc2 =FinalClass(13)      # Not an even number, set a as '2' now!

    [print(func)
            for func in fc2.__dir__()
            # for func in FinalClass.__dir__(fc2)
            # if not func.startswith("_")
            ]

    [print(fc._FinalClass__a)
            for fc in [fc1, fc2]
            ]

def c_run():
    """Simple Answer from STACKOVERFLOW"""
    c = C()
    c.x = 'foo'  # setter called!
    foo = c.x    # getter called!
    del c.x      # deleter called!
    pass

def age_getter_setter():
    """
    # This is Atom Editor's default snippet - {new}property
    #   - # TODO: don't know how to use
    """
    doc = "The age_getter_setter property."

    # property(doc, fget, fset, fdel)
    # If use below, locals become 5, not 4, which cause Err,

    # def __init__(self, age=0):
    #     self._age_getter_setter = age

    def fget(self):
        print("fget() called!")
        return self._age_getter_setter

    def fset(self, value):
        print("fset() called!")
        self._age_getter_setter = value

    def fdel(self):
        print("fdel() called!")
        del self._age_getter_setter

    return locals()



class Movie(object):
    """
    # [파이썬] get/set 속성값과 프로퍼티(property)
    # https://whatisthenext.tistory.com/115
    """
    def __init__(self, movie_name):
        # hidden variable
        self.__movie_name = movie_name
        self.__before_name = ""

    @property
    def movie_name(self):
        """변수처럼 사용하지만, 사실은 매서드를 사용해서 변수를 변경한다"""
        # 이때 메서드 이름은 변수(속성)이름과 동일하게 하는 것이 좋습니다.
        # 변수를 호출했을때, 히든변수에 담긴 값을 반환하도록 설정하는것
        # 변수처럼 사용하기 위해 데코 @property 를 사용한다.
        print("getter method called!")
        return self.__movie_name

    @movie_name.setter
    def movie_name(self, new_movie_name):
        """ 히든 속성(영화명)을 메서드를 통해서 변경한다 setter 메서드"""
        # 이때 메서드 이름은 변수(속성)이름과 동일하게 하는 것이 좋습니다.
        # 변수처럼 바뀌는 속성을 지정하기 위해서 @property.setter 를 사용한다.

        # 히든속성을 바꾸기 전에, BEFORE(히든) 속성에 저장후 바꾼다.
        print("setter method called!")
        self.__before_name , self.__movie_name = self.__movie_name, new_movie_name

        echoes = [
            f"=== CHANGE PROPERTY BY SETTER ===",
            f" - BEFORE: {self.__before_name}",
            f" - AFTER : {self.movie_name}",
            f"..................................",
            f"\n\n",
        ]

        [print(echo) for echo in echoes]


class GeeksForGeeks(object):
    """ SIMPLE PROPERTY SETTING!
    # Geeks for Geeks - Getter & Setter in Python
    # https://www.geeksforgeeks.org/getter-and-setter-in-python/
    """
    # In Python, getters and setters are not the same as those in other
    # OOP languages. Basically, the main purpose of using getters & setters in
    # OOP is to ensure data encapsulation.
    # Private variables in python are not actually hidden fields like in
    # other OOP. Getters and Setters in python are often used when:
    #   - use getters & setters to add validation logic around getting &
    #     setting a value.
    #   - To avoid direct access of a class field i.e. private variables
    #     cannot be accessed directly or modified by external user.
    def __init__(self, age=0):
        self._age = age

    def get_age(self):
        """getter method"""
        print("getter method called!")
        return self._age

    def set_age(self, x):
        print("setter method called!")
        self._age = x

    def del_age(self):
        print("deleter method called!")
        del self._age

    # property() 실행전(kay) / 실행후(jay) get/set 방법!
    age = property(get_age, set_age, del_age)


class Geeks(object):
    """ OTHER PROPERTY SETTING! - use property decorator!
    # Geeks for Geeks - Getter & Setter in Python
    # https://www.geeksforgeeks.org/getter-and-setter-in-python/
    """
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        print("getter method called!")
        return self._age

    @age.setter
    def age(self, age):
        if age < 18:
            object_name = self.__class__.__name__
            print(f"'{object_name}' is not permitted, under age of 18!")
        else:
            print("setter method called!")
            self._age = age


class SampleClass(object):
    """
    # Property vs. Getters and Setters in Python
    # https://www.datacamp.com/community/tutorials/property-getters-setters
    """
    # Table Of Contents
    #   1. What Are Getters And Setters
    #   2. Private Attribute - Encapsulation
    #   3. Property
    def __init__(self, a):
        ## private varibale or property in Python
        self.__a = a

    ## getter method to get the properties using an object
    def get_a(self):
        print("getter method called!")
        return self.__a

    ## setter method to change the value 'a' using an object
    def set_a(self, a):
        """
        # condition to check whether 'a' is suitable or not
        # only accept, even number which is greater than 0
        """
        if a > 0 and a % 2 == 0:
            print(f"Accepted!, set a as '{a}' now!")
            self.__a = a
        else:
            print("Not an even number, set a as '2' now!")
            self.__a = 2
        print("setter method called!")


class FinalClass(object):
    """
    # Make the setter and getter methods as private to hide them.
    # Property vs. Getters and Setters in Python
    # https://www.datacamp.com/community/tutorials/property-getters-setters
    """
    def __init__(self, var):
        ## calling the set_a() method to set the value 'a' by checking certain conditions
        self.__set_a(var)

    ## getter method to get the properties using an object
    def __get_a(self):
        print("getter method called!")
        return self.__a

    ## setter method to change the value 'a' using an object
    def __set_a(self, var):
        ## condition to check whether var is suitable or not
        if var > 0 and var % 2 == 0:
            print(f"Accepted!, set a as '{var}' now!")
            self.__a = var
        else:
            print("Not an even number, set a as '2' now!")
            self.__a = 2
        print("setter method called!")

    a = property(__get_a, __set_a)


class C(object):
    """
    # simple anser from STACKOVERFLOW
    # https://stackoverflow.com/questions/2627002/
    # whats-the-pythonic-way-to-use-getters-and-setters
    """
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        print("getter of x called!")
        return self._x

    @x.setter
    def x(self, value):
        print("setter of x called!")
        self._x = value

    @x.deleter
    def x(self):
        print("deleter of x called!")
        del self._x


if __name__ == '__main__':
    main()
