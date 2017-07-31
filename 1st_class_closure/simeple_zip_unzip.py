#
#
#

sentence ="aab"

count= 0
num= 1
bofore= ''
result= ''

for n in sentence:

    if count == 0:
        before= n
        count= 1

    else:
        if before != n:
            if num == 1:
                num=''
            result += (before + str(num))
            before= n
            num = 1
        else:
            num += 1

def main():
    print('before= %s' % sentence) # before
    print('after = %s' % result)   # after
    print('compression ratio= %.1f %%' % (100*len(result)/len(sentence)))

if __name__ == '__main__':
    main()
