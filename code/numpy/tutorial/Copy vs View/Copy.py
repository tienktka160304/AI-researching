import numpy as np

arr = np.array([1, 2, 3, 4])
x = arr.copy()
arr[0] = 42

print(arr) #output = [42  2  3  4]
print(x) #output = [1  2  3  4]