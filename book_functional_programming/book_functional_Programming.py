""" Page.54 - High order funtion """
year_cheese = [
    (2007,38.98),
    (2008,32.76),
    (2009,27.78),]

def highOrderFunction():
    """  """
    print(max(year_cheese))                         # (2009, 27.78)  : yc[0]
    print(max(year_cheese, key=lambda yc: yc[1]))   # (2007, 38.98)  : yc[1]
    print(max(map(lambda yc: (yc[1], yc), year_cheese)))
    # (38.98, (2007, 38.98)) : 'list' and 'function'
# highOrderFunction()

def trueOrFalseTest():
    """ strict or generous judgment """
    0 and print("True")         # 0 = False
    True and print("True")      # True - True
    True and print("Right!")    # as you see...
# trueOrFalseTest()

# ----------------------------------------------------------------------
""" Page.58 - Lazy funtion """
def numbers():
    """ Lazy function = not available at first. """
    for n in range(1024):
        print("=", n)
        yield n                 # wait until call again.
# numbers()           # yield until call again

def sumUpto(num):
    """ call lazy function 'numbers' then numbers() kicked in
        at first planed to 1024, but yields
        at second, call again upto 10
    """
    sum = 0
    for n in numbers():
        if n == num:
            break
        sum += 1
    return sum
sumUpto(8)

# -----------------------------------------------------------------------
""" first class function example.01 """
def isPrimer(n):
    def isPrime(k, coprime):
        """ is k relatively prime to the value of coprime? """
        if k < coprime**2:
            return True
        if k % coprime == 0:
            return False
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
    return isPrime(n, 3)
# isPrimer(10)
