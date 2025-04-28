import numpy as np

a1 = np.array([[1,2], [3,4]])

a2 = np.array([[5,6], [7,8]])

a = np.concatenate((a1,a2),axis=1)

print(a)
#output = [[1 2 5 6]
 #         [3 4 7 8]]
 
 
#if axis = 0 : output =
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]