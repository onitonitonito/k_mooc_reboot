""" EXERCISE - ATTRIBUTES AND METHODS
Write an object oriented program to create a precious stone.
Not more than 5 precious stones can be held in possession at a given point
of time.

If there are more than 5 precious stones, delete the first stone and store
the new one.
"""
class PreciousStone(object):
    # this is class attribute, (not self)
    number_of_precious_stones = 0
    precious_stone_collection = []

    def __init__(self, name):
        self.name = name
        PreciousStone.number_of_precious_stones += 1

        if PreciousStone.number_of_precious_stones <= 5:
            PreciousStone.precious_stone_collection.append(self)
        else:
            del PreciousStone.precious_stone_collection[0]
            PreciousStone.precious_stone_collection.append(self)

    @staticmethod
    def display_precious_stones():
        for precious_stone in PreciousStone.precious_stone_collection:
            print(precious_stone.name, end = ', ')
        print()

precious_stone_1  = PreciousStone("Ruby")
precious_stone_2  = PreciousStone("Emerald")
precious_stone_3  = PreciousStone("Sapphire")
precious_stone_4  = PreciousStone("Diamond")
precious_stone_5  = PreciousStone("Amber")

precious_stone_5.display_precious_stones()

precious_stone_6 = PreciousStone("Onyx")
precious_stone_6.display_precious_stones()
