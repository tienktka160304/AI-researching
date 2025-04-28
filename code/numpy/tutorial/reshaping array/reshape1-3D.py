import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr = arr.reshape(2,3,2)
# 2 dimensions - 3 subdimensions - 2 elements.
print(newarr) #output = [[[ 1  2]
#                         [ 3  4]
#                         [ 5  6]]

#                        [[ 7  8]
#                         [ 9 10]
#                         [11 12]]]