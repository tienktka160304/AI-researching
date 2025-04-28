import numpy as np

arr = np.array([1, 2, 3, 4])

x = arr.copy()
y = arr.view()

print(x.base) #output = None
print(y.base) #output = [1 2 3 4]