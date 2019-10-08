# This function must take in a list of integers and 
# return the corresponding list of look and say numbers
def get_las_list(inputlist):
    
    # Loop through each integer in the list to get the corresponding
    # look and say number
    return([ get_las_k(x) for x in inputlist ])
    
# Test - try your function on the below
print(get_las_list([10, 1, 4])) # This should give [13211311123113112211, 1, 1211]