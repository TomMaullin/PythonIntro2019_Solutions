# Read
triangular = np.loadtxt('04_numpy/triangle.txt')

# Save shape
tri_shape = triangular.shape

# Reshape
triangular = triangular.reshape(1, triangular.shape[0]*triangular.shape[1])

# Get the numbers 1 to length(triangular)
n = np.arange(triangular.shape[1])+1

# Work out what the triangular numbers should be
triangular_correct = n*(n+1)/2

# Find the value where triangular does not each triangular correct
print(np.where(triangular_correct!=triangular))
print(triangular[np.where(triangular_correct!=triangular)])

# Save Triangular_correct to file
np.savetxt('04_numpy/triangle.txt', 
           triangular_correct.reshape(tri_shape),
           fmt='%.0f')