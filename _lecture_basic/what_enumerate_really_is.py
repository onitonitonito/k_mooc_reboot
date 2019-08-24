""" WHAT ENUMERATE REALLY IS?
# Enumerate in Python - Just learn Python
# http://bit.ly/2ZiV3Vz
#
"""
print(__doc__)


from assets.config_asset import names
from assets.class_asset import run

class RunEnumerate(object):
    def show_how_it_works(self, en):
        """01. BASIC ENUMERATE ITERATION
        - enumerate class explanations in detail
        """

        en = enumerate(names)

        print(enumerate)    # <class 'enumerate'>
        print(en)           # <enumerate object at 0x000001C5C8C9CDC8>

        # print(dir(en))    # __next__, __iter__
        # en.__next__()

        print(iter(en))     # <enumerate object at 0x0000022EE6F5CDC8>

        print(next(en))     # return (0, 'Tom')
        print(next(en))     # return (1, 'Karl')
        print(next(en))     # return (0, 'William')
        print(next(en))     # return (0, 'Jonathan')
        # print(next(en))     # StopIteration

        # print(en.__next__())# return next tuple - (iter, item)
        # print(en.__next__())# return (2, 'William')
        # print(en.__next__())# return (3, 'Jonathan')
        # print(en.__next__())# StopIteration

        # =======     the 2 different way to run Iteration     =======
        #
        # Traceback (most recent call last):
        #   File "C:...\what_enumerate_really_is.py", line 29, in <module>
        #     print(en.__next__())# return next tuple - (iter, item)
        # StopIteration
        #
        # [Finished in 0.182s]
        #
        # ============================================================

        return [(i, name) for i, name in enumerate(names)]

re = RunEnumerate()



if __name__ == '__main__':
    run(func=re.show_how_it_works)

    pass
