import os

FILE_NAME = '_1_thadd_article.pdb'
DESTIN_DIR = os.path.join(os.path.dirname(__file__), FILE_NAME)

f = open(DESTIN_DIR, 'r', encoding='UTF-8')
a = f.read()        # 'str'
f.close()

b = a.split('\n^+^+^\n')        # list
c = b[1].split("'\\n")

for n in range(1, len(c)):
    if '@donga.com' in c[n]:
        print('%s = %s '%(n,c[n]))
        break
    else:
        print('%s = %s '%(n,c[n]))
