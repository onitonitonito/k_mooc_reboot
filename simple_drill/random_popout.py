"""
# Learn how it works - pop() / remove()
  - array.pop(positon) - pop-out(delete) & return data
  - array.remove(number) - search & remove number
"""
# print(__doc__)
import random

end = 10


def main():
    (array_01, array_02) = list(range(1, end + 1)), list(range(1, end + 1))
    repeat_pop_of(array_01)
    repeat_remove_of(array_02)


def random_pop(array):
    """
     array.pop(position) - pop-out(delete) array in POS. of array & return it
     (해당위치의 데이터를 뽑아내고, 뽑아내는 숫자를 리턴한다.)
     """
    positon = random.randint(0, len(array) - 1)
    # position selected!

    print(f"pop({positon})!({array.pop(positon):>2}) ... {array}")
    # when pop() is called, Show(return) and Remove


def random_remove(array):
    """
    array.remove(position) - search 1st position & delete. if not, raise Err.
    (첫번째 위치의 데이터를 삭제한다.)- 없으면 ValueError:  x not in list
    """
    number = random.choice(array)
    # data selected

    array.remove(number)
    # Just Remove, not show.

    print(f"remove!({number:>2}) ... {array}")


def print_deco(func):
    """ 실행func 주변을 화려하게 데코레이션(테코레이터) """
    def inner(args):
        """ 본func의 args, kwargs 를 인수로 전달한다 """
        print(f"array= {args}")
        print("-------------------")

        func(args)

        print("-------------------")
        print(f"array= {args} \n")
    return inner


@print_deco
def repeat_pop_of(array):
    for x in range(len(array)):
        random_pop(array)


@print_deco
def repeat_remove_of(array):
    for x in range(len(array)):
        random_remove(array)




if __name__ == '__main__':
    main()
