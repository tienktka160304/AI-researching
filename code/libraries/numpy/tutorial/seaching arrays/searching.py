import numpy as np

a = np.array([1,2,3,4,5,6,6,2])

x = np.where(a % 2 == 0)

print(x)
#output = (array([1, 3, 5, 6, 7], dtype=int64),)