
def square_numbers(list_):
    """ generator function """
    result= []
    for n in list_:
        result.append(n**2)
    return result

nums= [1, 3, 5, 7, 9,]
square_list= square_numbers(nums)

_a= nums
_b= type(square_list)
_c= square_list

print(dir(square_numbers(nums)))
print()

print(square_numbers(nums).__doc__)
print(square_numbers(nums).__str__)
print()

print('input_list  = ',_a)
print('square_type =', _b)
print('square_list =', _c)
