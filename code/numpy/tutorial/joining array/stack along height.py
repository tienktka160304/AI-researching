import numpy as np

a1 = np.array([1,2,3])

a2 = np.array([4,5,6])

a = np.dstack((a1,a2))

print(a)
#output = [[[1 4]
        #   [2 5]
        #   [3 6]]]