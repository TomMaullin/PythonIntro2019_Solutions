def lyapunov(A,B,C):
    
    # Work out n
    n = A.shape[0]
    
    # Get vec(C)
    vecC = mat2vec(C)
    
    # Get (I kron A)
    IkronA = np.kron(np.eye(n),A)
    
    # Get (B^T kron I)
    BtkronI = np.kron(B.T, np.eye(n))
    
    # Get vec(X)=(I kron A + B^T kron I)^(-1)vec(C)
    vecX = np.linalg.inv(IkronA+BtkronI) @ vecC
    
    # Convert vecX back to X
    X = vec2mat(vecX)
    
    return(X)