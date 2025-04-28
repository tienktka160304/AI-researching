import numpy as np

aee = np.array([1, 2,3,4], dtype="S")

print(aee) #output = [b'1' b'2' b'3' b'4']
print(aee.dtype) #output = |S1

arr = np.array([1, 2, 3, 4, 5, 6], dtype='i4')
# i = i4 = 32 | i1 = 8 | i2 = 16 | i8 = 64 
print(arr) #output = [1 2 3 4]
print(arr.dtype) # output = int32