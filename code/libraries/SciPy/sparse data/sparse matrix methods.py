import numpy as np
from scipy.sparse import *

a = np.array([[0,0,0], [0,0,1],[1,2,3]])

print(csr_matrix(a).data)
# [1 1 2 3] - list the not zero items