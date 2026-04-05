def decode_permission_bits(read_bit, write_bit, execute_bit):
    result = False
    if read_bit > 0 or write_bit > 0 or execute_bit > 0:
         result = True

    number = (read_bit * 4) + (write_bit * 2)+ (execute_bit * 1)
             
    
    
         
    return number, result
        
