def get_middle_items(items):
    middle = []
    if len(items) >= 3:
        middle = items[1:len(items)-1]
        print(middle)
    return middle
