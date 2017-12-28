
from numpy import *

A = mat([[1,2,2],[3,2,1]])
eigvals,eigVects = linalg.eig(A * A.T)
print(A * A.T)
print(A.T * A )
print(eigvals)
print(eigVects)
print(A.T * eigVects)
eigvals,eigVects = linalg.eig(A.T * A)
print(eigvals)
print(eigVects)
print(A * eigVects)
#print(A)
#print(A.T)
