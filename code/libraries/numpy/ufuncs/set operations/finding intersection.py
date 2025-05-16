import numpy as np

a = np.array([1,2,3,4])
b = np.array([3,4,5,6])

print(np.intersect1d(a,b, assume_unique=True))
#[3 4]