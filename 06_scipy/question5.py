
# ----------------------------------------------------------------------------
#
# This, and question 4, actually were questions on the SIAM 2002 hundred 
# dollar hundred digit challenge:
#
# https://en.wikipedia.org/wiki/Hundred-dollar,_Hundred-digit_Challenge_problems
#
# ----------------------------------------------------------------------------

# This function must return the value of f(x,y)
def my_g(alpha):
    
    # Function for the inside of the integral
    def innerFunc(alpha, x):
        
        return((2+np.sin(10*alpha))*x**alpha*np.sin(alpha/(2-x)))
    
    # Perform the integral of the inner function as a function of x
    result = integrate.quad(lambda x: innerFunc(alpha, x), 0, 2,tol=1e-10)[0]
    
    return(result)

print(my_g(3))

# ----------------------------------------------------------------------------

# Turn the maximization problem into a minimization problem!
def negative_my_g(alpha):
    return(-my_g(alpha))

# Maximize g
result=optimize.minimize(negative_my_g, x0=2.5, bounds=optimize.Bounds(0, 5, keep_feasible=False), method='Powell')

# ----------------------------------------------------------------------------
#
# If you have attempted this question you have no doubt realized that there is
# something going wrong with the numerical approximation here! This is due to 
# the sin(alpha/(2-x)) expression in the integral. As x goes to 2, alpha/(2-x)
# goes to infinity and the sine function increases in frequency! This is a 
# problem especially when we get close to 2. e.g. it does something like this:
#
# https://2aih25gkk2pi65s8wfa8kzvi-wpengine.netdna-ssl.com/hs/files/2017/12/sin_reciprocal_x2.png
#
# To truly solve this problem you need some heavy mathematics, see:
#
# https://mathworld.wolfram.com/Hundred-DollarHundred-DigitChallengeProblems.html
#
# We can get close though, by making an assumption that only a small amount is
# to be added to the integral from the interval [2-epsilon,2] for small enough
# epsilon. This isn't a wholy unreasonable assumption, given that the sine 
# function alternates but to prove this would need a lot of formal mathematics
# for rigourous justification! 
#
# ----------------------------------------------------------------------------
# This function must return the value of f(x,y)
def my_g(alpha):
    
    # Function for the inside of the integral
    def innerFunc(alpha, x):
        
        return((2+np.sin(10*alpha))*x**alpha*np.sin(alpha/(2-x)))
    
    # Perform the integral of the inner function as a function of x
    result = integrate.quad(lambda x: innerFunc(alpha, x), 0, 2-1e-3)[0]
    
    return(result)

# ----------------------------------------------------------------------------

# Turn the maximization problem into a minimization problem!
def negative_my_g(alpha):
    return(-my_g(alpha))

# Maximize g
result=optimize.minimize(negative_my_g, x0=2.5, bounds=optimize.Bounds(0, 5, keep_feasible=False), method='Powell')

# ----------------------------------------------------------------------------
#
# The true maximal g can be found at 0.785933674. The above code will give
# 0.78627135. Congratulations if you got close to these values! 
#
# ----------------------------------------------------------------------------

my_g(0.785933674)