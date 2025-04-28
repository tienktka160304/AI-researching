import numpy as np

arr = np.array([1, 2, 3, 4])
x = arr.view()
x[0] = 23

print(arr) #output = [23  2  3  4]
print(x) #output = [23  2  3  4]