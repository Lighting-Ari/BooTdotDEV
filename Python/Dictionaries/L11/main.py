def merge(dict1, dict2):
    new_dict = {}
    for name in dict1 :
        new_dict[name] = dict1[name]
    for name in dict2:
        new_dict[name]= dict2[name]
        
    return new_dict

    
