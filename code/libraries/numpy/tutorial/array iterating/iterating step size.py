import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8]])

for x in np.nditer(a[:, ::2]):
#run from 0 - end dimension, from 0-end subdimension, from index = 0 - end with step = 2
    print(x)
#output = 1
#         3
#         5
#         7