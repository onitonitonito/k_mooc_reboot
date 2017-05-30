def get_morse_code_dict():
    morse_code = {
        "A": ".-",      "B": "-...",    "C": "-.-.",   "D": "-..",  "E": ".",
        "F": "..-.",    "G": "--.",     "H": "....",   "I": "..",   "J": ".---",
        "K": "-.-",     "L": ".-..",    "M": "--",     "N": "-.",   "O": "---",
        "P": ".--.",    "Q": "--.-",    "R": ".-.",    "S": "...",  "T": "-",
        "U": "..-",     "V": "...-",    "W": ".--",    "X": "-..-", "Y": "-.--",
        "Z": "--..",
        "0":"-----",    "1":".----",    "2":"..---",    "3":"...--", "4":"....-",
        "5":".....",    "6":"-....",    "7":"--...",    "8":"---...","9":"----.",
    }
    return morse_code

def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %-10s" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message

def is_help_command(user_input):
    result = user_input.upper()
    if result == 'H' or result == 'HELP':
        return True
    else:
        return False

def is_validated_english_sentence(user_input):
     # skipping letters, ( without decoding )
    input_validate = False

    for i in user_input:
        if i.isalpha == True:
            input_validate = True

        elif i == '.' or i == ',' or i == '!' or i == '?' or i == ' ':
            continue

        else:
            return False

    if input_validate == True:
        return True
    else:
        return False

def is_validated_morse_code(user_input):

    input_validate = False
    for i in user_input:
        if i == '-' or i == '.' or i == ' ':
            continue
        else:
            return False

    for i in user_input.split():
        if i in get_morse_code_dict().values():
            input_validate = True
        else:
            return False

    if input_validate == True:
        return True
    else:
        return False

def get_cleaned_english_sentence(raw_english_sentence):
    result = raw_english_sentence
    result = result.replace('.', '')
    result = result.replace(',', '')
    result = result.replace('!', '')
    result = result.replace('?', '')
    result = result.strip()
    return result

def decoding_character(morse_character):
    morse_code_dict = get_morse_code_dict()
    for key, value in morse_code_dict.items():
        if value == morse_character:
            return key

def encoding_character(english_character):
    morse_code_dict = get_morse_code_dict()
    return morse_code_dict[english_character]

def decoding_sentence(morse_sentence):
    result = ''
    string = morse_sentence.replace('  ', ' * ')
    for i in string.split(' '):
        if i == '*':
            result += ' '
            continue
        result += decoding_character(i)
    return result

def encoding_sentence(english_sentence):
    result = ''
    string = get_cleaned_english_sentence(english_sentence)
    for i in string.split():
        for j in i:
            result += encoding_character(j.upper())
            result += ' '
        result += ' '
    return result

def main():
    print("Morse Code Program!!")

    while True:
        user_input = input('Input your message(H - Help, 0 - Exit): ').upper()
        if user_input == '0':
            break

        elif user_input == 'H' or user_input == 'HELP':
            print(get_help_message())

        elif is_validated_english_sentence(user_input) == True:
            print(encoding_sentence(user_input))

        elif is_validated_morse_code(get_cleaned_english_sentence(user_input)) == True:
            print(decoding_sentence(user_input))

        else:
            print('Wrong Input')

    print("Good Bye\nMorse Code Program Finished!!")

if __name__ == "__main__":
    main()

# https://github.com/seomin3/kmooc-python/blob/master/lab_8/morsecode.py
# http://www.mykit.com/kor/ele/morse.htm
