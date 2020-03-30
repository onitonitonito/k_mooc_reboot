"""
# calculate exact PHI using Archimedes method
"""
# differences between inner/outer poligon's surrounding lengthes

print(__doc__)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pyprnt import prnt

NUM_REPEAT = 16
RADIOUS = 0.2
ECHO = False

def main():
    poligon_dict = get_dict_lengths_poligons(NUM_REPEAT, RADIOUS, ECHO)
    # prnt(poligon_dict)      # FOR TEST

    last_key = list(poligon_dict.keys())[-1]
    print(poligon_dict[last_key])

    df_01 = pd.DataFrame.from_dict(poligon_dict).T
    df_01.columns = ['inner','outer','delta']
    df_01.plot(grid=True, figsize=(6,8))

    plt.title(
            f"upto '{NUM_REPEAT}'- Poligons inner/outer " +\
            f"length comparison [r='{RADIOUS}']"
        )
    plt.xlabel('n-th poligons')
    plt.ylabel('length around poligons')

    plt.show()

def get_length_around_poligon(num_poligon, pos='inner', radious=1, echo=True):
    """ HELPER() for get_dict_lengths_poligons() """
    if num_poligon < 3 :
        print("*** ERR: NUM_POLIGON SHOULD BE GREATER THAN '3'! ***")
        return False

    theta = 360 / (2 * num_poligon)
    radian = np.deg2rad(theta)

    if pos == 'inner':
        value_trigonal = np.sin(radian)
    elif pos == 'outer':
        value_trigonal = np.tan(radian)
    else:
        print("*** ERR: unclassified poligon position - choose inner/outer")

    length_side = (2 * radious * value_trigonal)
    length_around = num_poligon * length_side

    if echo:
        print(f"theta            = {theta}")
        print(f"radian           = {radian}")
        print(f"value_trigonal   = {value_trigonal}")
        print(f"length_side      = {length_side}")

    return length_around

def get_dict_lengths_poligons(num_repeat, radious=1, echo=True):
    """ get_dict_lengths_poligons(num_repeat):
    # get dict = { num_poligon : [len_inner, len_outer, delta_in_out]}
    # len(dict) ... repeat from 3 to n-poligon
    """
    dict_poligon = {}

    for poligon in range(3, num_repeat+1):
        inner = get_length_around_poligon(poligon, 'inner', radious, echo)
        outer = get_length_around_poligon(poligon, 'outer', radious, echo)

        dict_poligon[poligon] = [inner, outer, outer-inner]

    return dict_poligon



if __name__ == '__main__':
    main()
