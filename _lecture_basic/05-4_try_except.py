""" ----------------------------- CHAPTER.05 LESSON.04--- Try, except, finally
    try, except... except, else, finally, raise Error
"""

""" 01 """
def test01_what_kind():
    try :
        n = 1000
        while True:
            n += 1
            print('{:,}'.format(n))

            if n >= 15_000:
                break
        print()

        f = open ('_a.txt', 'r')    # FileNotFoundError
        c = 4/0                     # ZeroDivisionError
        c = a[4]                    # NameError

    except FileNotFoundError as e:
        print('FileNotFoundError')
        print(e)

    except FileExistsError as e:
        print('FileExistsError')
        print(e)

    except EnvironmentError as e:
        print('EnvironmentError')
        print(e)

    except EOFError as e:
        print('EOFError')
        print(e)

    except ZeroDivisionError as e:  # 1
        print('ZeroDivisionError')
        print(e)

    except IOError as e:
        print('IOError')
        print(e)

    except NameError as e:
        print('NameError')
        print(e)

    except IndexError as e:
        print('IndexError')
        print(e)

    else:
        f = open('_a.pdb', mode='r', encoding='UTF-8')
        data = f.readline()
        print(data)

    finally:
        f.close()

    """ BaseException (Examples)
     +-- SystemExit
     +-- KeyboardInterrupt
     +-- GeneratorExit
     +-- Exception
          +-- StopIteration
          +-- StopAsyncIteration
          +-- ArithmeticError
          |    +-- FloatingPointError
          |    +-- OverflowError
          |    +-- ZeroDivisionError
          +-- AssertionError
          +-- AttributeError
          +-- BufferError
          +-- EOFError
          +-- ImportError
               +-- ModuleNotFoundError
          +-- LookupError
          |    +-- IndexError
          |    +-- KeyError
          +-- MemoryError
          +-- NameError
          |    +-- UnboundLocalError
          +-- OSError
          |    +-- BlockingIOError
          |    +-- ChildProcessError
          |    +-- ConnectionError
          |    |    +-- BrokenPipeError
          |    |    +-- ConnectionAbortedError
          |    |    +-- ConnectionRefusedError
          |    |    +-- ConnectionResetError
          |    +-- FileExistsError
          |    +-- FileNotFoundError
          |    +-- InterruptedError
          |    +-- IsADirectoryError
          |    +-- NotADirectoryError
          |    +-- PermissionError
          |    +-- ProcessLookupError
          |    +-- TimeoutError
          +-- ReferenceError
          +-- RuntimeError
          |    +-- NotImplementedError
          |    +-- RecursionError
          +-- SyntaxError
          |    +-- IndentationError
          |         +-- TabError
          +-- SystemError
          +-- TypeError
          +-- ValueError
          |    +-- UnicodeError
          |         +-- UnicodeDecodeError
          |         +-- UnicodeEncodeError
          |         +-- UnicodeTranslateError
          +-- Warning
               +-- DeprecationWarning
               +-- PendingDeprecationWarning
               +-- RuntimeWarning
               +-- SyntaxWarning
               +-- UserWarning
               +-- FutureWarning
               +-- ImportWarning
               +-- UnicodeWarning
               +-- BytesWarning
               +-- ResourceWarning
    """

# test01_what_kind()


""" 02 """
class CustomError(Exception):
    def __init__(self, n=99):
        if n == 1:
            self.msg = 'This is # 1st. stupid Error'

        elif n == 2:
            self.msg = 'This is # 2nd. follish Error'

        elif n == 3:
            self.msg = 'This is # 3rd. idiotic Error'

        else:
            self.msg = 'THIS IS UNKNOWN STUPID BEHAVEIOR!...'

    def __str__(self):
        return self.msg

def say_nick(nick):
    if nick == 'idiot':
        raise CustomError(1)
    print('Your nick is %s'% nick)

def test02_custom_err_msg():
    say_nick('idiot')         #
    raise CustomError(3)        # n=3
    raise CustomError           # n=99
# test02_custom_err_msg()


""" 03 """
def test03_if_deal_with_str_OK():
    while True:
        _a = input("Try again? Yes=Enter / No='Q'")

        if _a.lower() == 'q':
            break
        elif _a == '':
            print('you punch [Enter] key, means go...')
        else:
            print(' %s means ... go'% _a)

        print('\n\n\n')
        print('OK...!')
        print("Let's go again")
test03_if_deal_with_str_OK()

def test03_but_deal_with_int_NG():
    while True:
        try:
            _n = input('input number will show you : 100-n   \n')

            answer = 100 - int(_n)
            print('100 - %s = %s'% (_n, answer))
            print('\n\n\n')

        except:
            if str(_n).lower() == 'q':
                break
            else:
                print('WRONG INPUT! - Try Again')
                print('\n\n\n')
# test03_but_deal_with_int_NG()
