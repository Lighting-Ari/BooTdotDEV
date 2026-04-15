def divide_list(nums, divisor):
    new_list=[]
    for num in nums :
        new_list.append(num/divisor)
    return new_list
        
"""
Assignment
Complete the divide_list() function. It takes a list and a number as input, and should return a new list that contains all the elements of the original list after dividing them by the second input.

For example:

divided_list = divide_list([6, 8, 10], 2)
print(divided_list)
# [3.0, 4.0, 5.0]
"""