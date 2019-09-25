data='''
park 801213-1002345
kim  701212-1102112
'''

# -----------------------------------------------------------------
def blind_last_personal_info():
    ''' local variables (4)
    result[], line, word_result, word
    '''
    result = []
    for line in data.split("\n"):
        word_result = []

        for word in line.split(" "):
            if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
                word = word[:6] + "-" + "*"*7

            word_result.append(word)
        result.append(" ".join(word_result))
    print("\n".join(result))
# blind_last_personal_info()

# -----------------------------------------------------------------
def blind_last_using_RE():
    import re

    pat = re.compile("(\d{6})[-]\d{7}")
    print(pat.sub("\g<1>-*******", data))
# blind_last_using_RE()

# -----------------------------------------------------------------
def put_data_into_dict():
    ''' Local Varuables : (3)
    resrlt[], dict_result, dict_word
    '''
    result = data.strip().split("\n")

    for n in range(len(result)):
        print("%s = %s" %(n+1,result[n]))

    dict_result = {}
    for word in result:
        dict_word = word.split()
        dict_result[dict_word[0]] = dict_word[1]
    print(dict_result)
# put_data_into_dict()

# -----------------------------------------------------------------
def main():
    blind_last_personal_info()
    blind_last_using_RE()
    put_data_into_dict()


if __name__ == '__main__':
    main()
