"""
# finde duplicated number
given an array nums containing n+1 integers where each inter is between
 1 & n (inclusve)
prove that at least one duplicate num must exist. Assue that there is only
duplicate num but it could be repeated more than once.
find the duplicate one.

Example 1:
 - Input : [1,2,4,2,2]
 - Output: 2

Example 2:
 - Input : [1,3,4,6,6,6,5]
 - Output: 6

 * You must use only constant, 0(1) extra space.
 * You must not modify the array (assue the array is read only once)
 * Your runtime complexity should be less than 0(n2).

Floyd's Tortoise and Hare Algorithm
https://www.youtube.com/watch?v=pKO9UjSeLew&feature=youtu.be
"""
# tortoise & hare loop algorithm
# https://manducku.tistory.com/45

nums = [1,2,4,3,5,6,2]
nums = [1,3,4,6,6,6,5]

def main():
    print(find_duplicate(nums))
    print(find_hare_tortoise(nums))

def find_duplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return num
        seen[num] = True
    return seen

def find_hare_tortoise(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1


if __name__ == '__main__':
    main()
    pass
