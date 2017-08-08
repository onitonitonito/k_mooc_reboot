def fx1():
    print("fx1...")

def fx2(a):
    print("fx2..", a)

def fx3(a, b):
    print("fx3...", a, b)

def fx4(a=3, b=4):
    print("fx4..", a, b)

def fx5(a, b, c=11, d=33):
    print("fx5..", a, b, c, d)

def fx6(a, b_list):
    print("fx6..", a)
    for x in b_list:
        print(x)


ff2 = []

def add_callback(callback, *args, **kw):
    print(callback, args, kw)
    """
    <function fx1 at 0x022CDC00> () {}
    <function fx4 at 0x022D61E0> (93,) {}
    <function fx4 at 0x022D61E0> (93,) {'b': 777}
    <function fx5 at 0x022D6198> (91, 92) {'c': 93, 'd': 94}
    <function fx6 at 0x022D6150> (11, [100, 101, 102]) {}
    """
    ff2.append((callback, args, kw))

def run_fx2(ff):
    # print("ff2 = ", ff)
    for callback, arg, kw in ff:
        callback(*arg, **kw)        # callback = function

# MAKE EXECUTE LIST in ff2 (f=exe + f2=callback)
add_callback(fx1)
add_callback(fx4, 93)
add_callback(fx4, 93, b=777)
add_callback(fx5, 91, 92, c=93, d=94)
add_callback(fx6, 11, [100, 101, 102])

run_fx2(ff2)

"""
fx1...
fx4.. 93 4
fx4.. 93 777
fx5.. 91 92 93 94
fx6.. 11
100
101
102
"""
