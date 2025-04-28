import numpy as np

a1 = np.array([1,2,3,4,5])
a2 = np.array([5,6,7,8,9])

print(np.power(a1,a2))
#[      1      64    2187   65536 1953125]
#[    1^5     2^6     3^7     4^8     5^9]