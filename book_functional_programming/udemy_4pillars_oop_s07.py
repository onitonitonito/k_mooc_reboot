"""
# Section.4 / lecture-07
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
