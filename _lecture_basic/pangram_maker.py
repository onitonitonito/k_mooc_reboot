"""
# Pangram maker both English & Korean
# http://timothylive.net/pangram_maker.php
"""
# print(__doc__)

def get_chars_length(quote):
    """ count without space, only alpha """
    chars_dense = (quote.replace(" ", "")).lower()
    length =  len(chars_dense)
    return length, chars_dense

def get_index_false(bool_array):
    array_index_false = []
    count_false = bool_array.count(False)

    for n in range(count_false):
        index_false = bool_array.index(False)
        array_index_false.append(index_false)
    return array_index_false

def check_english_pangram(quote_english):
    """ English Pangram Algorithm """
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    length, chars_dense =  get_chars_length(quote_english)

    checks_general = [ length > 26, chars_dense.isalpha() ]
    checks_alpha = [chars_dense.count(alpha) > 0 for alpha in alphas]

    print(checks_alpha.count(False))
    print(checks_alpha)

    judge_index = get_index_false(checks_alpha)

    # return checks_alpha.count(False) is 0, alphas[int(*judge_index)]
    return checks_alpha.count(False) is 0, judge_index

def what_the(array_numbers):
    total = 0

    for i in array_numbers:
        total = total + i

    count = len(array_numbers)
    average = total / count

    return average, total, count


if __name__ == '__main__':
    quote_english="The quick brown fox jumps over lazy dog"     # 0 - True
    quote_english="the quick brown fox jumped over lazy"        # 2 - g,s

    length, chars = get_chars_length(quote_english)
    print(length, chars)

    check = check_english_pangram(quote_english)
    print(check)
