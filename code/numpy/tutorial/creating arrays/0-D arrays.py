import numpy as np

arr_0D = np.array(42)
#create a 0-D array with value 42
print(arr_0D) #output = 42

arr_1D = np.array([1, 2, 3])
#create  a 1-D array
print(arr_1D) #output = [1 2 3]

arr_2D = np.array([[1, 2, 3], [13, 2, 4]])
#create a 2-D array
print(arr_2D) #ouput = [[ 1  2  3]
                    #   [13  2  4]]
                    
arr_3D = np.array([[[1, 2, 3], [5, 6, 7]], [[8, 9, 10], [13, 2, 4]]])
#create a 3-D array

print(arr_3D) #output = [[[ 1  2  3]
                    #     [ 5  6  7]]

                    #    [[ 8  9 10]
                    #     [13  2  4]]]