def divisors(k):
    
    # List 1...k
    divisors = np.arange(1,k+1)
    
    # Keep numbers that divide k perfectly
    divisors = divisors[k%divisors==0]
    
    return divisors