import numpy as np

a1 = np.array([1,2,3])

a2 = np.array([4,5,6])

a = np.stack((a1,a2), axis=1)

print(a)
#output = [[1 4]
#          [2 5]
#          [3 6]]


#if axis = 0: output = [[1 2 3]
#                       [4 5 6]]