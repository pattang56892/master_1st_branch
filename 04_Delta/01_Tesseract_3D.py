import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data points for the tesseract
theta = np.linspace(0, 2 * np.pi, 15)
phi = np.linspace(0, np.pi, 15)
psi = np.linspace(0, np.pi, 15)
tau = np.linspace(0, 2 * np.pi, 15)
r = 1

x = r * np.outer(np.cos(theta), np.sin(phi))
y = r * np.outer(np.sin(theta), np.sin(phi))
z = r * np.outer(np.ones_like(theta), np.cos(phi))
w = r * np.outer(np.cos(tau), np.sin(psi))
v = np.linspace(-r, r, 15)

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
