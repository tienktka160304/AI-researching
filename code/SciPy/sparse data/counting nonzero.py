import numpy as np
from scipy.sparse import *

a = np.array([[0,0,0],[1,2,3],[3,4,5]])

print(csr_matrix(a).count_nonzero())
# 6