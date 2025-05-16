import numpy as np

a1 = np.array([1,2,3,4])
a2 = np.array([5,6,7,8])

print(np.prod([a1,a2], axis=1))
# [  24 1680]