import numpy as np

a = np.array([1,2,3,4,5,6])

arr = np.array_split(a, 4)

print(arr[0]) #output = [1 2]
print(arr[1]) #output = [3 4]
print(arr[2]) #output = [5]
print(arr[3]) #output = [6]