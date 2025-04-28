import numpy as np

a = np.array([2,3,4,5])
b = np.array([3,4,5,6])

print(np.setxor1d(a,b, assume_unique=True))
#[2 6]