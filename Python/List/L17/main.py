def get_champion_slices(champions):
    first_list = champions [2:]
    secon_list = champions [:-1] #secon_list = champions [:len(champions)-1]
    trhird_list = champions [::2]
    return first_list, secon_list, trhird_list
        
