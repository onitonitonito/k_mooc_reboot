"""
# functions : for a few initial path setting
"""
print(__doc__)

import os

def get_cut_dir(name_cut:str) -> str:
    dir_current = os.path.dirname(__file__)
    dir_cut = "".join(dir_current.partition(name_cut)[:2])
    return dir_cut





if __name__ == '__main__':
    """ for TEST! """
    dir_home = get_cut_dir('openCV_TAcademy')
    print(dir_home)
