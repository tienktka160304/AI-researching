import numpy as np
from scipy.sparse import *

a = np.array([[0,0,0],[0,10,20],[3,4,5]])

new=csr_matrix(a)

print(new)
#   (2, 0)        3
#   (1, 1)        10
#   (2, 1)        4
#   (1, 2)        20
#   (2, 2)        5