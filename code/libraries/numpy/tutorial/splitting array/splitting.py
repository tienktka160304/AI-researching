import numpy as np

a = np.array([1,2,3,4,5,6])

arr = np.array_split(a, 4)

print(arr)
#output = [array([1, 2]), array([3, 4]), array([5]), array([6])]