import numpy as np

a = np.array([10,15,25,5])

print(np.diff(a, n=3))
# [  5  10 -20]    n = 1
# [  5 -30]        n = 2
# [-35]            n = 3