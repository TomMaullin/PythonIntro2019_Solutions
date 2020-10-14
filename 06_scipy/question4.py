# This function must return the value of f(x,y)
def my_f(xy):
    
    # Get x and y
    x = xy[0]
    y = xy[1]
    
    # Work out the function
    result = np.exp(np.sin(50*x))+\
             np.sin(60*np.exp(y))+\
             np.sin(70*np.sin(x))+\
             np.sin(np.sin(80*y))-\
             np.sin(10*(x+y))+\
             0.25*(x**2+y**2)
    
    return(result)

print(my_f(np.array([1,1])))

# ----------------------------------------------------------------------------
# There are lots of options you could run for the second part of the question.
# Here are just a few examples.
# ----------------------------------------------------------------------------
result=optimize.minimize(my_f, x0=np.array([1,1]), method='Nelder-Mead')
print(result.x)
print(result.fun)

result=optimize.minimize(my_f, x0=np.array([0,0]), method='Nelder-Mead')
print(result.x)
print(result.fun)

result=optimize.minimize(my_f, x0=np.array([1,1]), method='Powell')
print(result.x)
print(result.fun)

result=optimize.minimize(my_f, x0=np.array([0,0]), method='Powell')
print(result.x)
print(result.fun)
# ----------------------------------------------------------------------------
# This, and question 5, actually were questions on the SIAM 2002 hundred 
# dollar hundred digit challenge:
#
# https://en.wikipedia.org/wiki/Hundred-dollar,_Hundred-digit_Challenge_problems
#
# It's very likely that you struggled to find the true global minima of the 
# function. The reason for this is that the surface is incedibly bumpy and
# there's lots of local minima that you might end up finding instead!
#
# Have a look at a picture of this function here:
#
# https://www.chebfun.org/examples/opt/GlobalMinimum.html
#
# This is an example of a use case when it might not be a great idea to use
# a generic optimizer!
#
# In case you were wondering the true minimum value is −3.306868647.
# ----------------------------------------------------------------------------