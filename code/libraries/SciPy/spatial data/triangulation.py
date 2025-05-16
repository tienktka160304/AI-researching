import numpy as np
from scipy.spatial import *
import matplotlib.pyplot as plt

points = np.array([
    [2,4],
    [2,7],
    [3,0],
    [3,6],
    [4,0]
])

simplices = Delaunay(points).simplices

plt.triplot(points[:,0], points[:,1], simplices)
#draw the line from point to point
plt.scatter(points[:,0],points[:,1], color='r')
#highlight the vertex = color

# the simplices property creates a generalization of the triangle notation.
plt.show()