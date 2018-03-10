def test(*args, **kwargs):
    parameters = ['', '*args', '**kwargs', '*args, **kwargs']
    a = 0
    if args: a += 1
    if kwargs: a += 2

    print("%s(%s)"% (test.__name__, parameters[a]))
    print('--------------------')
    print("1.args   = %s"% list(args))
    print("2.kweargs= %s\n"% dict(kwargs))

# test()
# test(1, 2, 3)
# test(i=4, j=5, k=6)
# test(1, 2, 3, i=4, j=5, k=6)

def decorator(normal_function):
    print("1.This is Sparta!")
    def wrapper(*buy_thing):
        print("2.AMAZON..!!")
        normal_function(buy_thing)
    return wrapper

@decorator
def where_can_i_buy_a(buy_thing):
    print("Where can I buy a '%s' ??!!"% buy_thing)

@decorator
def separator(buy_thing):
    print('--------------')

where_can_i_buy_a('New Computer')

separator()
