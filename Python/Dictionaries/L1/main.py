def get_character_record(name, server, level, rank):
    string_key = {
        "name" : name,
        "server" : server,
        "level" : level,
        "rank" : rank,
        # "id" : name + "#"+ server 
        "id" : f"{name}#{server}" 
    }

    return string_key
    
