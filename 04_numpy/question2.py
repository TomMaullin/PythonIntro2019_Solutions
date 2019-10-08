# Demean x
X_demeaned = (X-X.mean(axis=0))/X.std(axis=0)

# print/prove
print(X_demeaned.mean(axis=0))
print(X_demeaned.std(axis=0))

# Transpose X
Xt = X.T

# Demean and rescale
Xt_demeaned = (Xt-Xt.mean(axis=0))/Xt.std(axis=0)

# Transpose back
X_demeaned = Xt_demeaned.transpose()

# Print/prove
print(X_demeaned.mean(axis=1))
print(X_demeaned.std(axis=1))