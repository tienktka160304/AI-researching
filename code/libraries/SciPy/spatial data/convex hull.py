import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

# Define points
points = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1],
    [0.5, 0.5]
])

# Compute convex hull
hull = ConvexHull(points)

# Display simplices
print("Points:\n", points)
print("Simplices (edges):\n", hull.simplices)

# Visualize
plt.scatter(points[:, 0], points[:, 1], color='red')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')  # Draw edges
plt.legend()
plt.show()
# Points:                                Simplices (edges):
#  [[0.  0. ] -0                             [[1 0]   -line from 1 - 0
#  [1.  0. ]  -1                             [2 1]    -line from 2 - 1
#  [1.  1. ]  -2                             [3 0]    -line from 3 - 0
#  [0.  1. ]  -3                             [3 2]]   -line from 3 - 2
#  [0.5 0.5]]   -center 
