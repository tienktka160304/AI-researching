import numpy as np

arr = np.array([[1,2,3], [5,6,7]])

print(arr.reshape(-1)) #output = [1 2 3 5 6 7]
#or print(np.reshape(arr, 6))