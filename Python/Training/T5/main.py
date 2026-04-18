def total_valid_numbers(values):
    total = 0
    for value in values:
        try:
            total += int(value)
        except (ValueError, TypeError):
            continue
    return total

"""
Fix Total Valid Numbers
The total_valid_numbers function should add up all items that can be converted to integers.

If an item is invalid, it should skip that item and keep going.

Right now, the function has two problems:

it stops too early when it hits bad data
it returns the wrong thing at the end
Expected behavior
Return the total of all valid integer values in the list.

Invalid items like "cat" or None should be ignored.

For example:

values = ["10", "5", "cat", "8"]
print(total_valid_numbers(values))
# Expected: 23

more_values = [1, "2", None, "7"]
print(total_valid_numbers(more_values))
# Expected: 10

What to fix
Fix total_valid_numbers so that it:

tries to convert each item to an integer
skips invalid items with try/except
keeps processing the rest of the list
returns the final total

"""


