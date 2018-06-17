def show_ASCII_to127():
    COLUMN = 8
    for n in range(0, 124, COLUMN):
        for k in range(1, COLUMN+1, +1):
            i = n + k
            if (i == 9 or i == 13 or i == 10):      # exceptions
                character = " "                     # make blind
            else:
                character = chr(i)

            print('%s = %s'%(i, character), end="\t")

            if i >= 127:
                break
        print('\n')
show_ASCII_to127()
