a = '?name=pak&page=1&end=eof'

n = a.count('=')

for i in range(n):
    b = a.index('=')        # a.find('='), return POS
    print(b)
