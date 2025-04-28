import numpy as np
from scipy.sparse.csgraph import *
from scipy.sparse import *

a = np.array([
    [0,1,0,1],
    [1,1,1,1],
    [2,1,1,0],
    [0,1,0,1]
])

new = csr_matrix(a)

print(depth_first_order(new,1))
# (array([1, 0, 3, 2]), 
#  array([    1, -9999,     1,     0]))