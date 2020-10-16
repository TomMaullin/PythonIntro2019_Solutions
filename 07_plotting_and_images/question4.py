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

# Make a grid of values
X = np.arange(-5, 5, 0.05)
Y = np.arange(-5, 5, 0.05)
X, Y = np.meshgrid(X, Y)

# Get z
Z = my_f([X,Y])

from mpl_toolkits.mplot3d import Axes3D

# Make a 3D plot
fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface.
surf = ax.plot_surface(X, Y, Z,
                       linewidth=0, antialiased=False)

# Customize the axes
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Show the image
plt.show()