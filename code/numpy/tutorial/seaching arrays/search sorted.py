import numpy as np

arr = np.array([1,2,3,8,5,7])

x = np.searchsorted(arr, 7, side='right')

print(x)
#output = 3