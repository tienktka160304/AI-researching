import numpy as np

arr = np.array([1,2,3,4], ndmin = 5)

print(arr) #output = [[[[[1 2 3 4]]]]]

print(arr.ndim) #output = 5