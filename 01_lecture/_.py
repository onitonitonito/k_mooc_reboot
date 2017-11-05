
_str_1 = 'hello'
_s1_set = set(_str_1)
print(_s1_set)

_str_2 = 'how are you'
_s2_set = set(_str_2)
print(_s2_set, '\n\n')

""" (1) Union() """
union_ = _s1_set.union(_s2_set)
print(len(union_), union_)

""" (2) intersection() """
inter_ = _s1_set.intersection(_s2_set)
print(len(inter_), inter_)

""" (3) Difference(s2 - s1) """
differ_ = _s1_set.difference(_s2_set)
print(len(differ_), differ_)


_a = [1, 2, 3, 4]

for n in range(4):
    print(_a.pop())
