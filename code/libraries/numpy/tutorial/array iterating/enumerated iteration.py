import numpy as np

a = np.array([[1,2,3], [4,5,6]])

for idx, x in np.ndenumerate(a):
#idx : the position of x
    print(idx, x) 
#output = (0, 0) 1
#         (0, 1) 2
#         (0, 2) 3
#         (1, 0) 4
#         (1, 1) 5
#         (1, 2) 6