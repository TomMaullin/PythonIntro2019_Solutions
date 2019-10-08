# Here is some example input
exampleInput = [3,1,2,7]

# And it's expected output
expectedOutput = [2,1,1,13]

# Write your function here
def Fibonnaci(inputList):
    
    # Initial output list
    outputList = []
    
    for k in inputList:
        
        # If k is zero we add 0 to the list,
        # and if k is one we add 1 to the list
        if k==0 or k==1:
            
            outputList = outputList + [k]
        
        # Otherwise work out the fibonnaci numbers
        # by summing the previous
        else:
            
            # Fibonnaci two previous and one previous
            fib_2prev = 0 
            fib_1prev = 1
            
            # Current fibonnaci
            fib_curr = 1
            
            # Initial j
            j = 2
            while j < k:
                
                # Update fib_curr and prevs
                fib_2prev = fib_1prev
                fib_1prev = fib_curr
                fib_curr = fib_1prev + fib_2prev
                
                j = j + 1
                
            # Add the fibonnaci number output to the list
            outputList = outputList + [fib_curr]
    
    return(outputList)


# Check your answer against this expected output
print(Fibonnaci(exampleInput))
print(expectedOutput)