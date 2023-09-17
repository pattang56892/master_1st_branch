import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vertices of the tesseract (four-dimensional cube)
vertices = [
    [-1, -1, -1, -1],
    [-1, -1, -1, 1],
    [-1, -1, 1, -1],
    [-1, -1, 1, 1],
    [-1, 1, -1, -1],
    [-1, 1, -1, 1],
    [-1, 1, 1, -1],
    [-1, 1, 1, 1],
    [1, -1, -1, -1],
    [1, -1, -1, 1],
    [1, -1, 1, -1],
    [1, -1, 1, 1],
    [1, 1, -1, -1],
    [1, 1, -1, 1],
    [1, 1, 1, -1],
    [1, 1, 1, 1]
]

# Define the faces of the tesseract
faces = [
    [0, 1, 3, 2], [0, 4, 6, 2], [0, 1, 5, 4], [1, 3, 7, 5], [2, 3, 7, 6], [4, 5, 7, 6]
]

# Plot the tesseract
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for face in faces:
    x = [vertices[face[0]][0], vertices[face[1]][0], vertices[face[2]][0], vertices[face[3]][0]]
    y = [vertices[face[0]][1], vertices[face[1]][1], vertices[face[2]][1], vertices[face[3]][1]]
    z = [vertices[face[0]][2], vertices[face[1]][2], vertices[face[2]][2], vertices[face[3]][2]]
    w = [vertices[face[0]][3], vertices[face[1]][3], vertices[face[2]][3], vertices[face[3]][3]]

    for i in range(4):
        ax.plot([x[i], x[i]],
                [y[i], y[i]],
                [z[i], z[i]], [w[i], -w[i]], 'b')

    ax.plot(x + [x[0]], y + [y[0]], z + [z[0]], w + [w[0]], 'b')

# Set plot limits and labels
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Wireframe Illustration of a Tesseract')

# Show the plot
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vertices of the tesseract (four-dimensional cube)
vertices = [
    [-1, -1, -1, -1],
    [-1, -1, -1, 1],
    [-1, -1, 1, -1],
    [-1, -1, 1, 1],
    [-1, 1, -1, -1],
    [-1, 1, -1, 1],
    [-1, 1, 1, -1],
    [-1, 1, 1, 1],
    [1, -1, -1, -1],
    [1, -1, -1, 1],
    [1, -1, 1, -1],
    [1, -1, 1, 1],
    [1, 1, -1, -1],
    [1, 1, -1, 1],
    [1, 1, 1, -1],
    [1, 1, 1, 1]
]

# Define the edges of the tesseract
edges = [
    [0, 1], [0, 2], [0, 4], [1, 3], [1, 5],
    [2, 3], [2, 6], [3, 7], [4, 5], [4, 6],
    [5, 7], [6, 7], [8, 9], [8, 10], [8, 12],
    [9, 11], [9, 13], [10, 11], [10, 14], [11, 15],
    [12, 13], [12, 14], [13, 15], [14, 15], [0, 8],
    [1, 9], [2, 10], [3, 11], [4, 12], [5, 13],
    [6, 14], [7, 15]
]

# Plot the tesseract
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for edge in edges:
    x = [vertices[edge[0]][0], vertices[edge[1]][0]]
    y = [vertices[edge[0]][1], vertices[edge[1]][1]]
    z = [vertices[edge[0]][2], vertices[edge[1]][2]]
    w = [vertices[edge[0]][3], vertices[edge[1]][3]]

    ax.plot(x, y, z, w, 'b')

# Set plot limits and labels
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Wireframe Illustration of a Tesseract')

# Show the plot
plt.show()
