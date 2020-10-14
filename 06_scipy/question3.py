# This is the erf as a function of x
def my_erf(x):
    
    # Function for the inside of the integral.
    def innerFunc(y): 
        return(np.exp(-(y**2)))
    
    # Perform the integral of the inner function
    result = integrate.quad(innerFunc, 0, x)[0]
    
    # Multiply by 2/sqrt(pi)
    result = result*2/np.sqrt(np.pi)
    
    return(result)
    
print(np.allclose(my_erf(1),scipy.special.erf(1)))

print(my_erf(1),scipy.special.erf(1))