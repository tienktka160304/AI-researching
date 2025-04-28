import numpy as np

a = np.array([[1,2,3],[2,3,4],[3,4,5],[5,6,7],[7,8,9]])

arr = np.array_split(a, 5, axis=1)

print(arr)
# #output = 
# [array([[1],
#        [2],
#        [3],
#        [5],
#        [7]]), array([[2],
#        [3],
#        [4],
#        [6],
#        [8]]), array([[3],
#        [4],
#        [5],
#        [7],
#        [9]]), array([], shape=(5, 0), dtype=int32), array([], shape=(5, 0), dtype=int32)]