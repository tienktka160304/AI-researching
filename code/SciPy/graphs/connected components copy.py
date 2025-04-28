import numpy as np
from scipy.sparse.csgraph import *
from scipy.sparse import *

a = np.array([[0,1,2],[1,0,0],[2,0,0]])

new = csr_matrix(a)

print(connected_components(a))
#(1, array([0, 0, 0]))