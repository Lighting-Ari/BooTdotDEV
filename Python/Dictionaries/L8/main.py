def get_most_common_enemy(enemies_dict):
    enemy_name = None
    count = float("-inf")
    highest_count = float("-inf")

    for name in enemies_dict:
        count = enemies_dict[name]
        if count > highest_count :
            highest_count = count
            enemy_name = name
        
        
    return enemy_name
    
