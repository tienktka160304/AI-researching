import numpy as np

a = np.array([1,2,4,5,7])

x = np.searchsorted(a, [3,6],side='right')

print(x)
#output = [2 4]