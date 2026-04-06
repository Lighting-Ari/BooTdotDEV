def longest_uppercase_streak(text):
    current_streak = 0
    longest_streak = 0

    for char in text:
        if char >="A" and char <="Z": 
            current_streak += 1
            if current_streak > longest_streak :
                longest_streak = current_streak              
        else :
            current_streak = 0
            
    return longest_streak

 
