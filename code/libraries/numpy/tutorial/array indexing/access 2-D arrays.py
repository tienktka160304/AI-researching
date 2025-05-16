import numpy as np

arr = np.array([[1,2,3,4,5], [6, 7,8, 9, 10]])

print(arr[0, 1] + arr[1, 2]) #output = 10 <2 + 8>

arr_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr_3D[1,1,-2]) #output = 11