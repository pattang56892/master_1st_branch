import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the side length of the hexagon
side_length = 1

# Define the height of the hexagon
height = np.sqrt(3) * side_length

# Define the coordinates of the vertices of the hexagon
vertices = [
    [side_length, 0, 0],
    [side_length / 2, height / 2, 0],
    [-side_length / 2, height / 2, 0],
    [-side_length, 0, 0],
    [-side_length / 2, -height / 2, 0],
    [side_length / 2, -height / 2, 0]
]

# Convert the vertices to a numpy array
vertices = np.array(vertices)

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the hexagon
ax.plot(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='skyblue')

# Set plot limits and labels
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Illustration of a Regular Hexagon')

# Show the plot
plt.show()
