def filter_messages(messages):
    filtered_messages = []
    dang_counter = []

    for message in messages : # checking each str in the list
        
        words = message.split() # sepate eache word from individual str
        non_dang_messages = []
        dang_count = 0
        for word in words : # checking each word
            if word == "dang":
                dang_count += 1
            else :
                non_dang_messages.append(word)
        non_dang_messages = " ".join(non_dang_messages)
        filtered_messages.append(non_dang_messages)
        dang_counter.append(dang_count)
        
    return filtered_messages, dang_counter
        
            
    

