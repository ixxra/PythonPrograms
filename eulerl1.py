import numpy as np
A=[k for k in range(3,1000,3)]
B=[k for k in range(5,1000,5)]
C=set(A+B)
C=list(C)
np.sort(C)
print np.sort(C)
print sum(C)
