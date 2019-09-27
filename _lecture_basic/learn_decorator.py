"""
# Geek for Geek - http://bit.ly/2la2roe
# Decorators in Python
"""
# print(__doc__)



def main():
    #1st. -- 데코레이터 효과를 입히는 기본 방법 (번거롭다, 2줄)
    function = decorator(function_to_be_used)
    function()

    #2nd. -- 그래서 다음과 같이 표현할수 있다 @decorator
    factorial(8)

    #3rd. --  getting the value through return of the function
    print(f"Sum = {sum_two_numbers(1, 2)}")



""" 1st. example - basic """
def decorator(func):
    def inner1():
        print("Hello, this is before function execution")

        func()

        print("This is after function execution\n\n\n")
    return inner1


def function_to_be_used():
    print("This is inside the function !!")


""" 2nd. example - application """
import time
import math

def calculate_time(func):
    """
    # decorator to calculate duration - taken by any function.
    # added arguments inside the inner(),
    # if function takes any arguments, can be added like this.
    """
    def inner(*args, **kwargs):
        begin = time.time()

        func(*args, **kwargs)

        end = time.time()

        print("-----------------------------------")
        print(f"Total {func.__name__}({args[0]}) = {end - begin:.4} sec.\n\n\n")
    return inner


@calculate_time
def factorial(num):
    time.sleep(2)
    print(f"factorial({num}) = {math.factorial(num):,}")


"""3rd. example - """
def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        returned_value = func(*args, **kwargs)
        print("after Execution")
        print("------------")

        return returned_value
    return inner1


@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b





if __name__ == '__main__':
    main()
