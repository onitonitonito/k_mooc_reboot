from sys import path
from os.path import abspath, dirname
# path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


# print(path)     # <class 'list'> system path = []

path.append(dirname(abspath(dirname(__file__))))
# print(path)     # <class 'list'> system path = []

separator = '__'*20 + '\n' 
spath = path    # <class 'list'>
cpath = dirname(__file__)
ux1path = dirname(dirname(__file__))
ux2path = dirname(dirname(dirname(__file__)))
ux3path = dirname(dirname(dirname(dirname(__file__))))

print("NUM OF PATH= %s\n%s" % (len(spath), separator) )

for x in spath:     # system path <class 'list'>
    print(x)

print("%s\nLAST PATH= %s\n\n" % (separator,spath[-1]) )
# print(spath[0])
# print(spath[0])
print('cpath=   %s' % cpath)    # current path = os.path.dirname(__file__)
print('ux1path= %s' % ux1path)    # upper path = dirname(dirname(__file__))
print('ux2path= %s' % ux2path)   # upper-upper = dirname(dirname(dirname(__file__)))
print('ux3path= %s' % ux3path)   # upx3 path = dirname(dirname(dirname(dirname(__file__))))

# D:\My Documents\GitHub\K-Mooc\OOP_drill
# D:\My Documents\GitHub\K-Mooc
# D:\My Documents\GitHub
# D:\My Documents
# [Finished in 0.705s]
