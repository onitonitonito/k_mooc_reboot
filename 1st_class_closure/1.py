'''
####
# 1st Class function and Decorater
####
'''

def logger(msg):
    ''' 1st class function, arg(msg) will remains after (return:end)
    '''
    def say_msg ():
        print('say=',msg)

    return say_msg()

# log_hi = logger('Hi~!')
#
# print (log_hi)  # show OBJECT(say_msg) - instance & address
# log_hi()        # Method which runs logger('hi~!') function

print(logger('hihi'))
a = logger('hihi')
