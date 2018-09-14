import random

def flower(other_func):
    def wrapper(*args, **kwargs):
        print(" ...  I'll give you a @;>---   ...")
        print(args, kwargs, '\n')
        return other_func(*args, **kwargs)
    return wrapper

def decorator(other_func):
    def wrapper(*args, **kwargs):
        message = other_func(*args, **kwargs)
        print(''
            '--------- This is Decorator ------------\n'
            '   ... IT ALWAYS RUNS BEFORE HAND ...\n'
            '----------------------------------------\n'
            '  '+'%s'% message+ '\n'
            '----------------------------------------\n\n')
        # return other_func(*args, **kwargs)
    return wrapper






@flower
@decorator
def other_func(name, greeting='Hi???'):
    says = ['Nice to meet you!', 'How have you been?', "What's up?", "A-hoy!"]
    say = random.choice(says)
    return "{}! My name is '{}'! {}".format(greeting, name, say)




other_func('Emma', greeting='HELLO')



# if without 'DECORATOR' -----------
# a = decorator(other_func)
# a('kay', greeting='Say Hi')

# if with 'DECORATOR' ---------------
# other_func('Kay', greeting='HELLO')
# other_func('Jay', greeting='HI')

# repeatedly call funcs -------------
# other_func('Kay', 'HELLO')
# other_func('Jay', 'HI')

# using 'zip(seq1, seq2)' ---------------------
# names = 'Ai, Jay, Kay, El'.split(', ')
# says = 'HELLO, HI, SAY-YO, AH!'.split(', ')
# for name, say in zip(names, says):
#     other_func(name, greeting=say)
