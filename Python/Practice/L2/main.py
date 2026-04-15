def find_min(nums):
    my_variable = float("inf")
    for num in nums:
        if num < my_variable :
            my_variable = num
    

    return my_variable


"""Write a function called find_min() that finds the smallest number in a list. If the list is empty, return float("inf"). For example:

find_min([1, 3, -1, 2]) -> -1
find_min([18, 3, 7, 2]) -> 2"""