# Some random arbitrary matrices
A = np.random.randn(2,3)
B = np.random.randn(4,3)
C = np.random.randn(3,6)

# This should return a block diagonal matrix with A,B,C on
# the diagonals
def my_block_diag(A,B,C):
    
    # Work out the shapes of the input arrays
    shapes = np.array([A.shape, B.shape, C.shape])
    
    print(shapes)
    
    # Make an output array full of zeros
    D = np.zeros(np.sum(shapes, axis=0))

    # Work out where we want to put A,B and C in D
    rowinds = np.insert(np.cumsum(shapes[:,0]),0,0)
    colinds = np.insert(np.cumsum(shapes[:,1]),0,0)

    print(rowinds)
    
    # Add A
    D[rowinds[0]:rowinds[1],colinds[0]:colinds[1]]=A
    
    # Add B
    D[rowinds[1]:rowinds[2],colinds[1]:colinds[2]]=B
    
    # Add C
    D[rowinds[2]:rowinds[3],colinds[2]:colinds[3]]=C
    
    return D
    
# This is what you expect to get
D_expected = linalg.block_diag(A,B,C)

# This is what your function gives
D_test = my_block_diag(A,B,C)

# Let's see if their equal!
print('Did my function work: ', np.allclose(D_expected,D_test))