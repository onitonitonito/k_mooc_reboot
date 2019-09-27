"""
# How to use hint function in detail
# This module supports type hints as specified by PEP 484 and PEP 526.
# a few examples about typing — Support for type hints
# -------
# https://docs.python.org/3/library/typing.html
"""
#
# [파이썬] 파이썬의 타입 힌트
# https://artoria.us/35
# print(__doc__)

from typing import (List,
                    Dict,
                    Tuple,
                    )

# set alias : Type aliases using typing hint library
# - aliea use upper camel case = pascal case format.
Vector = List[float]
ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]

def main():
    names = ['kay', 'Sparx']
    # print(greeting(name='Kay'))
    # print(greeting(name='Suparx'))
    # [ print(greeting(chain_string)) for chain_string in ['kay', 'Sparx'] ]
    print(list(map(lambda x: greeting(x),['kay', 'Sparx'])))

    # typechecks; a list of floats qualifies as a Vector.
    # new_vector = scale(2.0, [1.0, -4.2, 5.4])

    # check format
    # print(new_vector)               # [2.0, -8.4, 10.8]
    # print(type(new_vector))         # <class 'list'>
    # print(Vector)                   # typing.List[float]


def greeting(name: str) -> str:
    """ var = name(str) / return = (str) """
    return f"Hello '{name}'!..."


def scale(scalar: float, vector: Vector) -> Vector:
    """
    var.1 = scalar(float),
    var.2 = vector(vector),
    retun =
    """
    return [scalar * num for num in vector]


def broadcast_message(message: str, servers: List[Server]) -> None:
    pass


def broadcast_message(
        message: str,
        servers: List[Tuple[Tuple[str, int], Dict[str, str]]]) -> None:
    """
    # The static type checker will treat the previous type signature as
    # being exactly equivalent to this one.
    """
    pass


if __name__ == '__main__':
    main()

    pass
