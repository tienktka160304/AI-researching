import numpy as np
from scipy.sparse import *

a = np.array([[0,0,0],[0,1,32],[3,4,5]])

mat = csr_matrix(a)
mat.eliminate_zeros()

print(mat)
#   (1, 1)        1
#   (1, 2)        32
#   (2, 0)        3
#   (2, 1)        4
#   (2, 2)        5