def get_zip(sentence):
    ar_sentence = list(sentence)
    result = ''

    for n in range(len(ar_sentence)):
        if n == 0:
            result += ar_sentence[n]
            num = 1
        else:
            if ar_sentence[n-1] == ar_sentence[n]:
                num += 1
            else:
                if num == 1 :
                    result += ar_sentence[n]
                else:
                    result += str(num) + ar_sentence[n]
                    num = 1
        # print("%s \t\t: num=%s" % (result, num)) -- checksum
    if num > 1:
        result += str(num)
    return (sentence, result)

def get_unzip(code):
    pass

def show_ratio(target, before, after):
    print()

    if target == 'zip':
        print("sentence = %s" % before)
        print("zipped   = %s" % after)
        print("compress = %2.1f%%" % (100 * len(after)/len(before)))

    elif target == 'unzip':
        print("compressed= %s" % before)
        print("unzipped   = %s" % after)
        print("compress = %2.1f%%" % (100 * len(after)/len(before)) )

    else:
        raise SystemExit('unknown target_name.. system\'s holt')

def main():
    string ="aaabbcbbbcchhhdddkkkfff"

    _a,_b = get_zip(string)
    show_ratio('zip', _a, _b)

if __name__ == '__main__':
    main()
