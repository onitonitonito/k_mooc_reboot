""" UDEMY LECTURE 04 - The 4 Pillars of Object-Oriented-Programming
 (1) U4-8 = 객체중의 self 파라메터 이해하기
 (2) U4-9 = 스태틱과 인스턴스 메쏘드
"""
SEPARATOR = '\n----- %s ---------'

def udemy4_7_class_n_instance_attribute():
    """ 인스턴스 속성 --> 클래스 속성 순서로 체크 한다.
      - 인스턴스 속성으로 신규작성 (인스턴스로 생성가능 = 용접공)
      - 클래스 속성은 수정 가능 (인스턴스로 수정가능 = 개인 정보만 수정)
    """
    class Employee(object):
        working_hour = 40               # 전역변수(클래스 변수)

        def __init__(self, name):
            self.name = name            # 전역변수(인스턴스 변수)

    kay = Employee('케이수팍스')         # 작업시간(클)/ 이름(매=인스턴스 속성)

    mark = Employee('마크맥고완')
    mark.working_hour = 45              # 기존정보 수정 (클래스 속성)
    mark.work_line = '용접공'            # 신규정보 추가 (인스턴스 속성)

    print(SEPARATOR% '고용자1 정보')
    print("'%s' 근무시간= %s Hr"% (kay.name, kay.working_hour))

    print(SEPARATOR% '고용자2 정보')
    print("'%s' 근무시간= %s Hr"% (mark.name, mark.working_hour))
    print("'%s' 의 전문분야 : %s" %(mark.name, mark.work_line))
# udemy4_7_class_n_instance_attribute()

def udemy4_8_understangind_self():
    """ self 파라미터의 이해 (인스턴스 전역변수 / 지역변수)
     - 매서드(함수) 내부 변수는 인스턴스로 호출 불가능 (self가 아닌 경우)
     - 매서드 내부에서만 사용할 수 있다 (당연한 이야기)
    """
    class Employee(object):
        def employee_details(self):
            self.name = "브라이언 매튜"
            print('Name(self) =', self.name)
            age = 30
            print('Age(none)  =', age)

        def show_employee_details(self):
            print('*** PRINT ANOTHER METHOD ***')
            print('이름(self) :', self.name)

            # NameError: name 'age' is not defined
            # print('나이(None)  :', age)        # ERROR!

            # AttributeError: 'Employee' object has no attribute 'age'
            # print('AGE(forced self)  :', self.age)    # ERROR!

    # kay = Employee()
    # kay.employee_details()
    # kay.show_employee_details()
# udemy4_8_understangind_self()

def udemy4_9_staticsmethod():
    """ """
    class Employee(object):
        def __init__(self):
            self.name = '마이클 오브라이언'

        def employee_details(self):
            print(SEPARATOR % '고용자 상세정보')
            print(' 1.이름(self) :', self.name)

        @staticmethod
        def welcome_message():
            """ '스태틱 매스드'는 딱히, 객체와 상관없다(self를 사용하지 않음)
             - 객체의 기능과 상관없지만, 구조(편의)상 클래스객체에 포함시킬 경우
             - '스태틱 매서드'를 호출 할 때는 인스턴스로 호출 할수 있다.
            """
            print(SEPARATOR % '스태틱 매소드(@staticmethod)')
            print("우리회사에 오신것을 환영합니다. -- 클래스객체와 무관합니다.")

            # self 를 정의하지 않았으므로, self로 혼용해서 쓸 수 없다.
            # NameError: name 'self' is not defined
            # print(" %s, 우리회사에 오신 것을 환영합니다!"% self.name)

    kay = Employee()
    kay.employee_details()

    # this is @staticmethod - decorator
    kay.welcome_message()
# udemy4_9_staticsmethod()

def udemy4_10_init_method_start():
    """ Create fully initialized Object
    """
    class Employee(object):
        def __init__(self, name):
            self.name = name

        # def enter_employee_details(self):
        #     self.name = '마크 맥거번'

        def display_employee_details(self):
            print(SEPARATOR% '고용자 상세정보')
            print(' 1.이름(self) :', self.name)


    kay = Employee('케이 수팍스')
    # kay.enter_employee_details()
    kay.display_employee_details()

    mark = Employee('마크 맥거번')
    # kay.enter_employee_details()
    mark.display_employee_details()
# udemy4_10_init_method_start()


# -------------------------------------------------------------------------
"""
# Section.4 / lecture-07 ~ 10
# Class Attributes & Instance Attributes
# Udemy lecture site (free)
# : https://www.udemy.com/python-oops-beginners/learn/v4/t/lecture/7359316
"""
class EmployeeVersionOne(object):
    working_hour = 45


employee_01 = EmployeeVersionOne()
employee_02 = EmployeeVersionOne()

def change_class_attr():
    """ CHANGE Class Attribute"""
    print(employee_01.working_hour) # 45
    print(employee_02.working_hour) # 45

    EmployeeVersionOne.working_hour = 30

    print(employee_01.working_hour) # 30     *** changed.
    print(employee_02.working_hour) # 30     *** changed.

    employee_01.working_hour = 20

    print(employee_01.working_hour) # 20     *** changed.
    print(employee_02.working_hour) # 30
# change_class_attr()

def add_instance_attr():
    """ ADD Instance atrr. to Class attr. """
    employee_01.name = 'John'
    print(employee_01.name)

    # print(employee_02.name) # Error - No Attributes in EmployeeVersionOne Class
    employee_02.name = 'Merry'
    print(employee_02.name)
# add_instance_attr()

# help(EmployeeVersionOne)                  # class object
# help(employee_01.name)          # str
# help(employee_02.working_hour)  # int



"""
# Section.4 / lecture-08
# Understanging the 'self' parameter
# Udemy lecture site (free)
# : https://www.udemy.com/python-oops-beginners/learn/v4/t/lecture/7359316
"""
class EmployeeInfomation(object):
    def employee_detail(self):
        global age
        print('*** show local inline ***')

        self.name = 'Matthew'
        print("Name = %s "% self.name)

        age = 30            # loval variabl
        print("Age = %s "% age, end='\n\n\n')

    def show_employee_detail(self):
        print('*** Pringting in another methode ***')
        print('Name : %s'% self.name)
        # can't use local variable -- claim global !!
        print('Age  : %s'% age, end='\n\n\n')


def main_understanding_self():
    """ 'self' = global in class and local """
    employee_03 = EmployeeInfomation()
    employee_03.employee_detail()
    employee_03.show_employee_detail()
# main_understanding_self()




"""
# Section.4 / lecture-09
# Section methods & Instance methods
# Udemy lecture site (free)
# : https://www.udemy.com/python-oops-beginners/learn/v4/t/lecture/7359320
"""

class EmployNameCall(object):
    """
    # Trap of Python : @classmethod vs. @staticmethod
    # subdescript - my head-over-heels confusion
    """
    def employee_detail(self):
        self.name = 'Ben'

    @staticmethod
    def welcome_message():
        print('welcome to our organization!')


employee_04 = EmployNameCall()
employee_04.employee_detail()
print(employee_04.name)
employee_04.welcome_message()
