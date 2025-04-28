import numpy as np 

a = np.array([1,2,3,4,5,6])

filter_a = a % 2 ==0

print(a)    #output = [1 2 3 4 5 6]
print(a[filter_a]) #output = [2 4 6]