def get_morse_dict():
    morse_dict = {
    "A": ".-",      "B": "-...",    "C": "-.-.",   "D": "-..",      "E": ".",
    "F": "..-.",    "G": "--.",     "H": "....",   "I": "..",       "J": ".---",
    "K": "-.-",     "L": ".-..",    "M": "--",     "N": "-.",       "O": "---",
    "P": ".--.",    "Q": "--.-",    "R": ".-.",    "S": "...",      "T": "-",
    "U": "..-",     "V": "...-",    "W": ".--",    "X": "-..-",     "Y": "-.--",
    "Z": "--..",

    "0":"-----",    "1":".----",    "2":"..---",    "3":"...--",    "4":"....-",
    "5":".....",    "6":"-....",    "7":"--...",    "8":"---..",   "9":"----.",

    ".":".-.-.-",    ",":"--..--",  "?":"..--..",   "/":"-..-.",    ":":"---...",
    "'":".----.",    "+":".-.-.",   "-":"-....-",   "=":"-...-",    "(":"-.--.",
    ")":"-.--.-",    "!":"-.-.--"
    }
    return morse_dict

def get_morse_chart():
    message = "\n"+("-"*60)+"\n"+"\tHELP - THE INT'L MORSE CODE CHART\n"+("-"*60)+"\n"
    morse_code = get_morse_dict()

    counter = 0

    for key in sorted(morse_code.keys()):
        counter += 1
        message += "%s: %-10s" % (key, morse_code[key])

        if counter % 5 == 0:
            message += "\n"

    return message + "\n"+"-"*60+"\n\n"

def get_morse_letter(arg_letter):
    morse_code = get_morse_dict()

    is_there = False
    for key in morse_code.keys():
        if key == arg_letter.upper():
            is_there = True
            return morse_code[arg_letter.upper()]
    return is_there

def get_morse_sentence(sentence):
    compose =""
    for x in range(len(sentence)):
        if sentence[x] != " ":
            compose += get_morse_letter(sentence[x]) + " "
        else:
            compose += "  "
    return str(compose)

def get_english_sentence(sentence):
    morse = get_morse_dict()

    b = sentence.split(" ")
    english = ""

    for x in range(len(b)):
        for key, value in morse.items():
            if b[x] == value:
                english += key

    return english


# http://www.mykit.com/kor/ele/morse.htm    --- about morse code
# http://admin0.github.io/morse/            --- morse converter

# ----- DICT type data handling -------------------------------------------
    #a = mc.keys()       # list = dict_keys(['A', 'B', 'C', 'D'
    #a = mc.values()     # list = dict_values(['.-', '-...', '
    #a = mc.items()      # list = dict_items([('A', '.-'), ('B', '-...'),
    #a = mc.get('!'.upper())    # SAME mc['!'.upper()] --- but KeyError: '!'
    #a = ( '!' in mc )   # List return FALSE.
    #
    #s = 'Life is short, you need python'
    #s1 = s.upper()
    #s2 = set(s1)        # Break STR into {list} form without repeatation
    #s3 = sorted(s2)     # s2.sort(), .insert('') .remove(''), .pop(n)
    #s3.remove(' ')      # .remove(n or S)=del., pop(n) = see & del.
    #
    #s3.pop(-1)
    #print(s3)
    #
    #if 'Y' in s3:
    #    s3.remove('Y')
    #    print(s3)
    #else:
    #    print(False)
    # ------------------------------------------------------------------------
