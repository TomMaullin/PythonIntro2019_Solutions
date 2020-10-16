# t function
def t(alpha,x):
    
    return(2+np.sin(10*alpha))*x**alpha*np.sin(alpha/(2-x))

# X values
xvals = np.linspace(0, 1.999, 256)

# Alpha values
alpha1 = 0.5
alpha2 = 1.5
alpha3 = 2.5
alpha4 = 3.5
alpha5 = 4.5

# t values
t1 = t(alpha1,xvals)
t2 = t(alpha2,xvals)
t3 = t(alpha3,xvals)
t4 = t(alpha4,xvals)
t5 = t(alpha5,xvals)

# This tells us that if we have 5 rows of plots and 1 column of plots,
# we want to put the next plot in the first position.
plt.subplot(5, 1, 1)
plt.plot(xvals,t1, '-')
plt.xlim(0, 2)

# This tells us that if we have 5 rows of plots and 2 column of plots,
# we want to put the next plot in the first position.
plt.subplot(5, 1, 2)
plt.plot(xvals,t2, '-')
plt.xlim(0, 2)

# This tells us that if we have 5 rows of plots and 3 column of plots,
# we want to put the next plot in the first position.
plt.subplot(5, 1, 3)
plt.plot(xvals,t3, '-')
plt.xlim(0, 2)

# This tells us that if we have 5 rows of plots and 4 column of plots,
# we want to put the next plot in the first position.
plt.subplot(5, 1, 4)
plt.plot(xvals,t4, '-')
plt.xlim(0, 2)

# This tells us that if we have 5 rows of plots and 5 column of plots,
# we want to put the next plot in the first position.
plt.subplot(5, 1, 5)
plt.plot(xvals,t5, '-')
plt.xlim(0, 2)