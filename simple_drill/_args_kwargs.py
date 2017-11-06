FINF_ARR = []

def fx1():
    print("fx1.. None")

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
    for i, args in enumerate(b_list):
        print('  L(%s) = %s' %(i, args))

def add_funcs(funcs, *args, **kw):
    """ append(funcs, args=tuple, kwargs=dict) in 'FINF_ARR'
    <function fx1 at 0x022CDC00> () {}
    <function fx4 at 0x022D61E0> (93,) {}
    <function fx4 at 0x022D61E0> (93,) {'b': 777}
    <function fx5 at 0x022D6198> (91, 92) {'c': 93, 'd': 94}
    <function fx6 at 0x022D6150> (11, [100, 101, 102]) {}
    """
    # print(funcs, args, kw)
    # # funcs = body, args_obj = tuple, kw_obj = dict

    FINF_ARR.append((funcs, args, kw))
    # print(FINF_ARR)

# MAKE EXECUTE LIST in FINF_ARR (f=exe + f2=funcs)
add_funcs(fx1)
add_funcs(fx4, 93)
add_funcs(fx4, 93, b=777)
add_funcs(fx5, 91, 92, c=93, d=94)
add_funcs(fx6, 11, [100, 101, 102])

for funcs, arg, kw in FINF_ARR:
    funcs(*arg, **kw)        # funcs = function

""" RESULTS
fx1.. None
fx4.. 93 4
fx4.. 93 777
fx5.. 91 92 93 94
fx6.. 11
  L(0) = 100
  L(1) = 101
  L(2) = 102
"""
