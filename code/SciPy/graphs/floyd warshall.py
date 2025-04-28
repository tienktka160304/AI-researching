import numpy as np
from scipy.sparse.csgraph import *
from scipy.sparse import *

a = np.array([
    [0,2,3],
    [2,0,0],
    [3,0,0]
])

new = csr_matrix(a)

print(floyd_warshall(new, return_predecessors=True))
# (array([[0., 2., 3.],
#        [2., 0., 5.],
#        [3., 5., 0.]]),
#  array([[-9999,     0,     0],      
#        [    1, -9999,     0],
#        [    2,     0, -9999]]))