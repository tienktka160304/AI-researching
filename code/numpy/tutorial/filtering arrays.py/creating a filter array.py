import numpy as np

a = np.array([1,2,3,4,5,6,7])

filter_a = []

for x in a:
    if x % 2 == 0:
        filter_a.append(True)
    else:
        filter_a.append(False)

arr = a[filter_a]

print(a)    #output = [1 2 3 4 5 6 7]
print(arr)  #output = [2 4 6]