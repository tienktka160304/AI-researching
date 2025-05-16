import numpy as np
from scipy.sparse.csgraph import *
from scipy.sparse import *

a = np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0]
])

new=csr_matrix(a)

print(dijkstra(new, return_predecessors=True))
# (array([[0., 1., 2.],
#        [1., 0., 3.],
#        [2., 3., 0.]]), 
#  array([[-9999,     0,     0],      
#        [    1, -9999,     0],
#        [    2,     0, -9999]]))
#(dist_matrix        , predecssors)
