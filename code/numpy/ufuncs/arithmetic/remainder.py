import numpy as np

a1 = np.array([10,20,30,40,50])
a2 = np.array([5,6,7,8,9])

print(np.mod(a1,a2))
#[0 2 2 0 5]
#[10%5 20%6 30%7 40%8 50%9]