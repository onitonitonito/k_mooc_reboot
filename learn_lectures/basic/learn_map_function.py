"""
# Python map() Function Explained & Visualized — Soshace • Soshace
# http://bit.ly/2ILOCFk - By Denis Kryukov - October 7, 2019
"""
import script_run

test_list = [
                "effort", "circle", "yearly", "woolen", "accept",
                "lurker", "island", "faucet", "glossy", "evader",
            ]

list_of_ds = [
                {
                    'user': 'Jane',
                    'posts': 18,
                },
                {
                    'user': 'Amina',
                    'posts': 64,
                },
            ]

lower_cases = [
                ['strength', 'agility', 'intelligence'],
                ['health', 'mana', 'gold'],
                ['armor', 'weapon', 'spell'],
            ]

def main():
    run_all_app()

def run_all_app():
    """HELPER(): needs this.module """
    import _map_function

    app_names = [
            func for func in _map_function.__dir__()
            if func.startswith("app")
            ]
    for i, app in enumerate(app_names):
        func = getattr(_map_function, app)
        print(f"\n\n\n*** {i+1}.APP NAME : {app}() ***")
        print(func.__doc__)
        print("-----"*10)
        func()

def app_01(word_list=test_list):
    """ALPHABETICAL ORDER = Avecefarian!"""
    value_list = []
    for item in test_list:
        value = is_abecedarian(item)
        value_list.append(value)

    value_list = [is_abecedarian(item) for item in test_list]
    results_list = map(is_abecedarian, test_list)

    # print(value_list)
    for item in test_list:
        if is_abecedarian(item):
            print(f"The word '{item}' ... is abecedarian. ;)")
        else:
            print(f"The word '{item}' is not abecedarian. :(")

def app_02(lower_cases=lower_cases):
    """map function - capitalize()"""
    map_object_01 = map(capitalize_word, lower_cases[0])
    map_object_02 = map(capitalize_word, lower_cases[1])
    map_object_03 = map(capitalize_word, lower_cases[2])

    test_list = list(map_object_01)
    test_set = set(map_object_02)
    test_tuple = tuple(map_object_03)

    print(test_list)
    print(test_set)
    print(test_tuple)

def app_03(list_of_ds=list_of_ds):
    """map object convertion to any form of data [list, tuple, set]"""
    _a = map(lambda x: x['user'], list_of_ds)  # Output: ['Jane', 'Amina']
    _b = map(lambda x: x['posts'] * 10, list_of_ds)  # Output: [180, 640]
    _c = map(lambda x: x['user'] == "Jane", list_of_ds)  # Output: [True, False]
    [print(item) for item in [list(_a), tuple(_b), set(_c)]]

def is_abecedarian(input_word):
    """
    # HELPWER: app_01() - ord(str) return charactor number
    # DEFINITION: if the word made by alphabatical order, abecedarian!
    """
    index = 0
    for letter in input_word[0:-1]:
        this_ord = ord(input_word[index])
        that_ord = ord(input_word[index + 1])
        # print(f"{index} : {this_ord} / {that_ord}")  # for test
        if this_ord > that_ord :
            return False
        else:
            index += 1
    return True

def capitalize_word(input_word):
    """# HELPER: app_02()"""
    return input_word.capitalize()



if __name__ == '__main__':
    print(__doc__)
    main()
