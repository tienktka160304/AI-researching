import numpy as np
from scipy.sparse import *

a = np.array([0,0,0,0,1,1,0,0,2])

print(csr_matrix(a))
#   (0, 4)        1
#   (0, 5)        1
#   (0, 8)        2