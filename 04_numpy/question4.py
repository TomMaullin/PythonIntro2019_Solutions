def mat2vec(matrix):
  
  #Return vectorised matrix
  return(matrix.transpose().reshape(matrix.shape[0]*matrix.shape[1],1))

# Use this example to test your code
matrix = np.random.randn(3,3)
print(matrix)
print(mat2vec(matrix))

def vec2mat(vec):
  
  # Return matrix
  return(vec.reshape(np.int64(np.sqrt(vec.shape[0])),np.int64(np.sqrt(vec.shape[0]))).transpose())

# Use this example to test your code
vec = np.array([[1,2,3,4]]).transpose()
mat = vec2mat(vec)
print(vec)
print(mat)