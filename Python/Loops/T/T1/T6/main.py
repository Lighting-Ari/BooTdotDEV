def get_boss_state(health, is_stunned):
    if health < 1:
        status = "defeated"
    elif is_stunned == True:
        status = "safe to attack"
    elif health < 20 and not is_stunned :
        status = "enraged"
    else :
        status = "fighting"

    return status
        
        
    
