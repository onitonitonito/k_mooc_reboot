import morse_code as mc
morse = mc.get_morse_dict()

sentence = " hello "
code = "... --- ..."

def get_upper_case(sentence):
    sentence = sentence.upper()
    sentence = sentence.strip()
    return sentence

def make_morse(sentence):
    sentence = get_upper_case(sentence)
    decode = ""
    for n in range(len(sentence)):
        if sentence[n] in morse:
            decode += morse[sentence[n]]+" "
        else:
            decode += "   "

    print("Sentence= %s" % sentence)
    print("Decoded = %s" % decode)

def make_english(code):
    decode = ""
    find_key=""
    num_fk=0

    arr_encode = code.split()
    arr_key = list(morse.keys())
    arr_value = list(morse.values())

    for n in range(len(arr_encode)):
        find_key = arr_encode[n]
        for x in range(len(arr_value)):
            if find_key == arr_value[x]:
                num_fk = x
                break
        decode += arr_key[num_fk]

    print("Code    = %s" % code)
    print("Sentence= %s" % decode)



def main():
    make_morse(sentence)
    print()
    make_english(code)

if __name__ == '__main__':
    main()
