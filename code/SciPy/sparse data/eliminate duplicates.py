import numpy as np
from scipy.sparse import csr_matrix

a = np.array([[0,0,0],[0,1,32],[1,1,2]])

mat = csr_matrix(a)
mat.sum_duplicates()

print(mat)
#   (1, 1)        1
#   (1, 2)        32
#   (2, 0)        1
#   (2, 1)        1
#   (2, 2)        2