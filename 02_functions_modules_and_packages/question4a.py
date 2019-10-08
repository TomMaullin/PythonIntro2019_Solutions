def next_las(las_k):
    
    # It is useful to have the character as a string
    # for this function
    las_k_str = str(las_k)
    
    # We need a counter to see how many times an 
    # element has occurred
    counter = 0
    
    # We need a string for the (k+1)th las number
    las_kplusone_str = ''
    
    # Initialize previous look and say digit we saw
    # to first digit
    prev_las_k_char = las_k_str[0]
    
    # We loop through each character counting how
    # many times it occurs
    for las_k_char in las_k_str:
        
        # If the last digit we saw is the same as this one
        if las_k_char == prev_las_k_char:
            
            # Increment the counter
            counter = counter + 1
        
        # If we have seen a new digit 
        else:
            
            # We now need to add how many times we saw the
            # last digit and the last digit itself to our 
            las_kplusone_str = las_kplusone_str + str(counter) + prev_las_k_char
            
            # Update the previous look and say character to our new character
            prev_las_k_char = las_k_char
            
            # Reset the counter
            counter = 1
    
    # We still need to add the last counter and digit
    las_kplusone_str = las_kplusone_str + str(counter) + prev_las_k_char
    
    # Convert our string back to an integer
    las_kplusone = int(las_kplusone_str)
    
    return(las_kplusone)