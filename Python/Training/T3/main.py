def build_seat_map(row_labels, seats_per_row, blocked_seats):
    available_seat = ""
    seat = 0
    count = 0
    

    for row in row_labels: 
        count += 1
        for seat in range(1,seats_per_row +1):
            temp_seat = row + str(seat)
            if temp_seat in blocked_seats:
                available_seat += "X" 
            else :
                available_seat +=  temp_seat 
            if seat < seats_per_row:
                available_seat += " "
                
        if count < len(row_labels):
            available_seat += "\n"
            
    return available_seat
                
            
            
