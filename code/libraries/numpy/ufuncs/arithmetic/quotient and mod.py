import numpy as np 

a1 = np.array([10,20,30,40,50])
a2 = np.array([5,6,7,8,9])

print(np.divmod(a1,a2))
#(array([2, 3, 4, 5, 5]), array([0, 2, 2, 0, 5]))