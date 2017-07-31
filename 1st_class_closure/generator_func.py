
def square_numbers(list_):
    result= []
    for n in list_:
        result.append(n * n)
    return result

nums= [1,3,5,7,9,]
square_list= square_numbers(nums)

_a= nums
_b= type(square_list)
_c= square_list
print('input_list= %s\nsquare_list:%s\n\t= %s' % (_a, _b, _c)
)
