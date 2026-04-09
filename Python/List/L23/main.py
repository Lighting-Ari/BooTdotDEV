def reverse_list(items):
    new_list = []
    for i in range(len(items)-1, -1,-1) :
        new_list.append(items[i])

    return new_list
        
