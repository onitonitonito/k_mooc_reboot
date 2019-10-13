"""
# Fun Functions: Bonus Lesson
# www.sketcherslodge.blogspot .com
# PYUNIVERSE Pychat
"""
# print(__doc__)

total = 4

def required_arg(n):
    """Required arguments"""
    total = n ** 2
    print(required_arg.__doc__, total)


def keyword_arg(str, num):
    """Keyword arguments"""
    total = str * num
    print(keyword_arg.__doc__, total)


def default_arg(name, age="i"):
    """Default arguments"""
    print(default_arg.__doc__, name, age)


def variable_length_args(arg, *var_tuple):
    """Variable-length arguments"""
    print(arg)
    for i in var_tuple:
        print(i)


#Anonymous arguments

required_arg(4)
keyword_arg(num=3, str="Ayo")
default_arg("me", 45)
variable_length_args(3,4,5,6,7,8)

print((lambda x: x**2)(6))
