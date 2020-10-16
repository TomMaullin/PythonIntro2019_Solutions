# ------------------------------------------------------------------
# First part
# ------------------------------------------------------------------
# Get a list of t values
t = np.linspace(-3*np.pi, 2*np.pi, 3000)

# Get x and y
x = t-1.6*np.cos(25*t)
y = t-1.6*np.sin(26*t)

# plot x against y
plt.plot(x, y)

# ------------------------------------------------------------------
# Second part
# ------------------------------------------------------------------
# Change to the directory
import os
os.chdir('07_plotting_and_images')

# Import the big function module
import bigFunction

# Get x and y
x,y=bigFunction.getxy(np.linspace(0, 96*np.pi, 3000))

# Plot x and y
plt.plot(x, y)

# Wa-hoo!