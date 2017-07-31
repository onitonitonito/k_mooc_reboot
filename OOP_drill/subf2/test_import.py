import sys
from os.path import dirname


# print(type(sys.path))       # <class 'list'>
# print (sys.path)            # numbers of path

# print(dirname(__file__))            # self folder
# print(dirname(dirname(__file__)))   # parent folder

print(sys.path)                     # before append
sys.path.append(dirname(dirname(__file__)))
print(sys.path)                     # after append
