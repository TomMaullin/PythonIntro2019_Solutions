# This function must take in an integer k and return the
# kth look and say number, l(k).
def get_las_k(k):
    
    # initial values
    las_k = 1
    k_current = 1
    
    # Loop through the las numbers getting the
    # next number each time
    while k_current < k:
        
        # Get next las
        las_k = next_las(las_k)
        
        # increment current k
        k_current = k_current + 1
        
    return(las_k)

# Test your function here:
print(get_las_k(1)) # This should give 1
print(get_las_k(2)) # This should give 11
print(get_las_k(5)) # This should give 111221
