VERB_DICT = {
    "say": say,
}

def get_input():
    commands = input(": ").split()
    verb_word = commands[0]         # say
    if verb_word in VERB_DICT:
        verb = VERB_DICT[verb_word]
    else:
        print("Unknown verb {}". format(verb_word))
        return

    if len(commands) >= 2:
        noun_word = commands[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))


def say(noun):
    return 'You said "{}"'.format(noun)



while True:
    get_input()
