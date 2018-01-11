""" EXERCISE - ATTRIBUTES AND METHODS
Write an object oriented program to create a precious stone.
Not more than 5 precious stones can be held in possession at a given point
of time.

If there are more than 5 precious stones, delete the first stone and store
the new one.
"""
class PreciousStone(object):
    number_of_precious_stones = 0
    precious_stone_collection = []

    def __init__(self, name):
        self.name = name
        # Increment the number of preciousStones
        PreciousStone.number_of_precious_stones += 1

        # Append the precious stone to the list if total number of stones are less than 5
        if PreciousStone.number_of_precious_stones <= 5:
            PreciousStone.precious_stone_collection.append(self)
        else:
            # If more than 5 stones are present, delete the first one and store the new one
            del PreciousStone.precious_stone_collection[0]
            PreciousStone.precious_stone_collection.append(self)

    @staticmethod
    def display_precious_stones():
        for preciousStone in PreciousStone.precious_stone_collection:
            print(preciousStone.name, end = ' ')
        print()

preciousStoneOne  = PreciousStone("Ruby")
preciousStoneTwo  = PreciousStone("Emerald")
preciousStoneThree  = PreciousStone("Sapphire")
preciousStoneFour  = PreciousStone("Diamond")
preciousStoneFive  = PreciousStone("Amber")

preciousStoneFive.display_precious_stones()

# Print all the stones after deleting the first stone
preciousStoneSix = PreciousStone("Onyx")
preciousStoneSix.display_precious_stones()
