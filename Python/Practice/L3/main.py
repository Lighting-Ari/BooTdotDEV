def remove_nonints(nums):
    new_list = []
    for num in nums:
        if type(num) is type(0):
            new_list.append(num)
    return new_list


"""
Assignment
Complete the remove_nonints() function. It takes a list and returns a new list but with all the non-integer types removed.

new_list = remove_nonints(["1", 1, "3", "400", 4, 500])
print(new_list)
# [1, 4, 500]
"""