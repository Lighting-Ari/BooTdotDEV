def join_strings(strings):
    new_str =""
    i = 0
    for str in strings:
        new_str = new_str + str 
        if i < len(strings)-1:
            new_str = new_str + ","
            i += 1
    return new_str


"""
# The world never deserved Tolkien

Assignment
Complete the join_strings() function. It takes a list of strings and returns a new single string. The new string is the concatenation of all the input strings from the list end-to-end, in order, with a comma between them. If the list is empty, return an empty string.

For example:

string_list = ["Annie", "Reiner", "Bertholdt"]
joined_string = join_strings(string_list)
print(joined_string)
# "Annie,Reiner,Bertholdt"

string_list = ["Eren", "Mikasa", "Armin"]
joined_string = join_strings(string_list)
print(joined_string)
# "Eren,Mikasa,Armin"
"""