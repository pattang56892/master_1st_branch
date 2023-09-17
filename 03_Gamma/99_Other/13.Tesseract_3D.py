import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data points for the tesseract
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)
psi = np.linspace(0, np.pi, 100)
tau = np.linspace(0, 2 * np.pi, 100)
r = 1

x = r * np.outer(np.cos(theta), np.sin(phi))
y = r * np.outer(np.sin(theta), np.sin(phi))
z = r * np.outer(np.ones_like(theta), np.cos(phi))
w = r * np.outer(np.cos(tau), np.sin(psi))
v = np.linspace(-r, r, 100)

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the tesseract
for i in range(len(v)):
    ax.plot_surface(x + v[i], y, z, color='skyblue', alpha=0.2)
    ax.plot_surface(x, y + v[i], z, color='skyblue', alpha=0.2)
    ax.plot_surface(x, y, z + v[i], color='skyblue', alpha=0.2)
    ax.plot_surface(w, y, z, color='skyblue', alpha=0.2)
    ax.plot_surface(x, w, z, color='skyblue', alpha=0.2)
    ax.plot_surface(x, y, w, color='skyblue', alpha=0.2)

# Set plot limits and labels
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Illustration of a Tesseract')

# Show the plot
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data points for the tesseract
t = np.linspace(0, 2 * np.pi, 100)
u = np.linspace(0, np.pi, 100)

# Create arrays for the coordinates of the tesseract's vertices
x = np.outer(np.cos(t), np.sin(u))
y = np.outer(np.sin(t), np.sin(u))
z = np.outer(np.ones(np.size(t)), np.cos(u))

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the tesseract
ax.plot_surface(x, y, z, color='skyblue', alpha=0.2)

# Set plot limits and labels
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Illustration of a Tesseract')

# Show the plot
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vertices of the tesseract
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
    ax.plot([vertices[edge[0]][0], vertices[edge[1]][0]],
            [vertices[edge[0]][1], vertices[edge[1]][1]],
            [vertices[edge[0]][2], vertices[edge[1]][2]], 'b')

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

# Define the vertices of the tesseract
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

# Define a color map based on the fourth dimension
colors = np.arange(len(vertices))

# Plot the tesseract with color variation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for edge, color in zip(edges, colors):
    ax.plot([vertices[edge[0]][0], vertices[edge[1]][0]],
            [vertices[edge[0]][1], vertices[edge[1]][1]],
            [vertices[edge[0]][2], vertices[edge[1]][2]], color='b', alpha=color / len(vertices))

# Set plot limits and labels
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Wireframe Illustration of a Tesseract with Color Variation')

# Show the plot
plt.show()