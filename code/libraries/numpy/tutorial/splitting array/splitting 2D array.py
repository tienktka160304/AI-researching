import numpy as np

a = np.array([[1,2],[3,4],[5,6],[7,8],[8,9]])

arr = np.array_split(a, 3)

print(arr[0])
#output=[[1 2]
#        [3 4]]
print(arr[1])
#output=[[5 6]
#        [7 8]]
print(arr[2])
#output=[[8 9]


#print(arr)output = [array([[1, 2],
    #            [3, 4]]), array([[5, 6],
    #            [7, 8]]), array([[8, 9]])]