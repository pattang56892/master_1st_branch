import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the side length of the pentagon
side_length = 1

# Calculate the apothem (distance from center to midpoint of a side)
apothem = side_length / (2 * np.tan(np.pi / 5))

# Calculate the radius of the circumscribed circle (distance from center to vertex)
radius = side_length / (2 * np.sin(np.pi / 5))

# Define the angles between each side of the pentagon
angles = np.linspace(0, 2 * np.pi, 6)[:-1]

# Create an array to store the vertices of the pentagon
vertices = []

# Calculate the vertices of the pentagon
for angle in angles:
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    z = 0
    vertices.append([x, y, z])

# Convert the vertices to a numpy array
vertices = np.array(vertices)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the pentagon
ax.plot(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='skyblue')

# Set plot limits and labels
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Illustration of a Regular Pentagon')

# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Define the side length of the pentagon
side_length = 1

# Calculate the angles between each side of the pentagon
angles = np.linspace(0, 2 * np.pi, 6)[:-1]

# Create an array to store the vertices of the pentagon
vertices = []

# Calculate the vertices of the pentagon
for angle in angles:
    x = side_length * np.cos(angle)
    y = side_length * np.sin(angle)
    vertices.append([x, y])

# Convert the vertices to a numpy array
vertices = np.array(vertices)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the pentagon
ax.plot(vertices[:, 0], vertices[:, 1], color='skyblue')

# Set plot limits and labels
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('2D Illustration of a Regular Pentagon')

# Show the plot
plt.show()
