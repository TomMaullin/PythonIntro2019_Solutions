def sumstrings(*args):
    
    # Work out the running sum
    runningsum = 0
    
    for arg in args:
        
        if arg.lower()=="one":
            
            runningsum = runningsum+1
            
        elif arg.lower()=="two":  
            
            runningsum = runningsum+2
        
        elif arg.lower()=="three":
            
            runningsum = runningsum+3
            
        if arg.lower()=="four":
            
            runningsum = runningsum+4
            
        if arg.lower()=="five":
            
            runningsum = runningsum+5
            
        if arg.lower()=="six":
            
            runningsum = runningsum+6
            
        if arg.lower()=="seven":
            
            runningsum = runningsum+7
            
        if arg.lower()=="eight":
            
            runningsum = runningsum+8

        if arg.lower()=="nine":
            
            runningsum = runningsum+9
            
        if arg.lower()=="ten":
            
            runningsum = runningsum+10
            
    return(runningsum)

print(sumstrings('one', 'one', 'nine',)) # This should give 11
print(sumstrings('one', 'two', 'seVen',)) # This should give 10