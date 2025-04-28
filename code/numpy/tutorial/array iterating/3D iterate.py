import numpy as np

arr = np.array([[[1,2,3],[4,5,6]], [[7,8,9], [10,11,12]]])

for x in arr:
    print(x)
#output = [[1 2 3]
#          [4 5 6]]
#         [[ 7  8  9]
#          [10 11 12]]

#to return the actual values :
for x in arr:
    for y in x:
        for z in y: 
            print(z)
#output =  1
#          ...
#          12