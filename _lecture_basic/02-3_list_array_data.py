""" ---------------------------------- CHAPTER.02 LESSON.03--- list(array)
  (1) list call = a[1], String slicing = a[:3] + '*' + a[3:]
  (2) list Slicing = a[3:5] = [4, 5]
  (3) list function =
"""

a = """
Kim KK = 001212-1009999
Lee HH = 041010-1111111
KIM pp = 731109-1020300
"""

def get_mask_info(str_unmasked):
    arr_data = str_unmasked.strip().split("\n")
    str_masked = ""

    for n in range(len(arr_data)):
        arr_data[n] = arr_data[n][:-6] + "*"*6
        str_masked = str_masked + arr_data[n] + "\n"

    return str_masked

def main():
    print(a)                    # original data <class 'str'>
    a_masked = get_mask_info(a) # masked_data

    print(type(a_masked))           # <class 'str'>
    print(a_masked)                 # masked String
# main()

""" ---------------------------------- CHAPTER.02 LESSON.03.1--- list(array)
  (1) list call = a[1], String slicing = a[:3] + '*' + a[3:]
  (2) list Slicing = a[3:5] = [4, 5]
  (3) list function =append(), sort(), reverse(), remove(), pop(), extend(), count()
"""

a = [1,2,3,4,4,4,4,5]

def test_01():
    print(type(a))
    print(a)
    print()
    #
    # a[0:2] = ['a', 'b']               # ['a', 'b', 3, 4, 5]
    # a[0:2] = ['a', 'b', 'c', 'd']     # ['a', 'b', 'c', 'd', 3, 4, 5]
    a[0:2] = ['a']                      # ['a', 3, 4, 5]
    a[0:2] = []                         # [3, 4, 5] - delete

    print(type(a))
    print(a)

def test_02():
    a.pop()
    print(a)

    a.remove(4)
    print(a)


""" ---------------------------------- CHAPTER.02 LESSON.03.1--- tupple & dictionary
 (1) tuple = skipped : just read chapter once.
 (2) Dict = UK (Unique Key) , Add: a['key'] = value, del(a[])
"""


a = { 'a':123213, 'b':1111, 3:123}

print(len(a))       # 3
print(a)            # { 'a':123213, 'b':1111, 3:123}
print(a[3])         # Call = 3 :123

a[3] = 100          # Exist = change value : 3:123 --> 3:100
print(a[3])         # call = 3 :100

a['key'] = 110      # {'a': 123213, 'b': 1111, 3: 100, 'key': 110}
print(a)

del a[3]
print(a)

print(a.keys())
print(len(a.keys()))
print(type(a.keys()))

print(a['key'])         # 110
print(a.get('key'))     # 110 - all the same. BUT......

# print(a['kiss'])         # KeyError : 'kiss'
print(a.get('kiss'))     # None
print(a.get('kiss','OUT OF DATA'))        # 'OUT OF DATA' - default value.

print("'key' in a=",   'key' in a)           # TRUE - Key value
print("'kiss' in a=", 'kiss' in a)           # FALSE - Key value
