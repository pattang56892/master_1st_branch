import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data points for the surface
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)
r = 1

x = r * np.outer(np.cos(theta), np.sin(phi))
y = r * np.outer(np.sin(theta), np.sin(phi))
z = r * np.outer(np.ones_like(theta), np.cos(phi))

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x, y, z, color='skyblue')

# Set plot limits and labels
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Illustration of Pi')

# Show the plot
plt.show()
