import numpy as np

a = np.array([[1,2], 
              [3,4]])
b = np.array([[2,0], 
              [1,2]])

print(a*b)
# [[2 0]
#  [3 8]]
print(a@b)
# [[ 4  4]
#  [10  8]]