import numpy as np

arr = np.array([1.2, 0, 4.9])

arr1 = arr.astype(bool)

print(arr1) #output = [ True False  True]
print(arr1.dtype) # output = bool