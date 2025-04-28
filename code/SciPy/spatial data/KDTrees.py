from scipy.spatial import *
import matplotlib.pyplot as plt

points = [(1,-1), (2,3), (-2,3), (2,-3)]

kd = KDTree(points)

res = kd.query((1,1))

distance, index = res

print(res)

plt.scatter(*zip(*points), color='b')
#zip(*points) transforms a list of tuples [(x1,y1),(x2,y2),..] into 2 separate tuples : (x1,x2,...) and (y1,y2,...)
plt.scatter(*(1,1), color ='r')

plt.show()