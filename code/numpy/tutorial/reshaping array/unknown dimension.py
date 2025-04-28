import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
near = arr.reshape(2,2,-1)

print(near) #output = [[[ 1  2  3]
#                       [ 4  5  6]]

#                      [[ 7  8  9]
#                       [10 11 12]]]
