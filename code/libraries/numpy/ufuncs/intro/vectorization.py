# x = [1,2,3,4]
# y = [3,4,5,6]
# z = []

# for i, j in zip(x,y):
#     z.append(i + j)
# print(z) #[4, 6, 8, 10]

import numpy as np
x = [1,2,3,4]
y = [3,4,5,6]
z = np.add(x,y)

print(z) #[ 4  6  8 10]