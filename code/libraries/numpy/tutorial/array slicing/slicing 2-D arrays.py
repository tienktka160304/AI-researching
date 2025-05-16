import numpy as np

arr = np.array([[1,2,3,4,5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4]) #output = [7 8 9]

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr1[0:2, 3]) #output = [4 8]

arr2 = np.array([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9]])

print(arr[0:2, 1:4]) #output = [[2 3 4]
                        #       [7 8 9]]