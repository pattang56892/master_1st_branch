import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the data for the planets
planets = {
    "Mercury": {"distance": 0.39, "radius": 0.038, "color": "gray"},
    "Venus": {"distance": 0.72, "radius": 0.095, "color": "bisque"},
    "Earth": {"distance": 1, "radius": 0.1, "color": "mediumturquoise"},
    "Mars": {"distance": 1.52, "radius": 0.053, "color": "indianred"},
    "Jupiter": {"distance": 5.20, "radius": 1.12, "color": "burlywood"},
    "Saturn": {"distance": 9.58, "radius": 0.945, "color": "khaki"},
    "Uranus": {"distance": 19.18, "radius": 0.401, "color": "lightskyblue"},
    "Neptune": {"distance": 30.07, "radius": 0.388, "color": "dodgerblue"}
}

# Create a figure and 3D axis
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Load the galaxy image as a background texture
galaxy_texture = mpimg.imread("C:/Users/patta/AppData/Local/Microsoft/WindowsApps/PY_3_Master/01_Projects/01_01_Project_Alpha/03_Gamma/galaxy.jpg")
x_vals = np.linspace(-35, 35, galaxy_texture.shape[1])
y_vals = np.linspace(-35, 35, galaxy_texture.shape[0])
x_mesh, y_mesh = np.meshgrid(x_vals, y_vals)
ax.plot_surface(x_mesh, y_mesh, np.zeros_like(x_mesh), rstride=1, cstride=1, facecolors=galaxy_texture, shade=False)

# Plot the Sun
ax.scatter(0, 0, 0, color='yellow', s=500, label="Sun")

# Plot the orbits and planets
for planet, data in planets.items():
    distance = data["distance"]
    radius = data["radius"]
    color = data["color"]
    theta = np.linspace(0, 2 * np.pi, 100)
    x = distance * np.cos(theta)
    y = distance * np.sin(theta)
    z = np.zeros_like(x)
    ax.plot(x, y, z, color=color)
    ax.scatter(distance, 0, 0, color=color, marker='o', s=100)
    ax.text(distance, 0, 0.05, planet, ha='center', color=color)

# Set the plot limits and labels
ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)
ax.set_zlim(-1, 1)
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')
ax.set_title('Solar System')
ax.legend()

# Remove ticks and spines
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Define the data for the planets
planets = {
    "Mercury": {"distance": 0.39, "radius": 0.038, "color": "gray"},
    "Venus": {"distance": 0.72, "radius": 0.095, "color": "bisque"},
    "Earth": {"distance": 1, "radius": 0.1, "color": "mediumturquoise"},
    "Mars": {"distance": 1.52, "radius": 0.053, "color": "indianred"},
    "Jupiter": {"distance": 5.20, "radius": 1.12, "color": "burlywood"},
    "Saturn": {"distance": 9.58, "radius": 0.945, "color": "khaki"},
    "Uranus": {"distance": 19.18, "radius": 0.401, "color": "lightskyblue"},
    "Neptune": {"distance": 30.07, "radius": 0.388, "color": "dodgerblue"}
}

# Create a figure and 3D axis
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Load the galaxy image as a background texture
galaxy_texture = mpimg.imread("C:/Users/patta/AppData/Local/Microsoft/WindowsApps/PY_3_Master/01_Projects/01_01_Project_Alpha/03_Gamma/galaxy.jpg")
ax.plot_surface([-35, 35], [-35, 35], [0, 0], rstride=1, cstride=1, facecolors=galaxy_texture, shade=False)

# Plot the Sun
ax.scatter(0, 0, 0, color='yellow', s=500, label="Sun")

# Plot the orbits and planets
for planet, data in planets.items():
    distance = data["distance"]
    radius = data["radius"]
    color = data["color"]
    theta = np.linspace(0, 2 * np.pi, 100)
    x = distance * np.cos(theta)
    y = distance * np.sin(theta)
    z = np.zeros_like(x)
    ax.plot(x, y, z, color=color)
    ax.scatter(distance, 0, 0, color=color, marker='o', s=100)
    ax.text(distance, 0, 0.05, planet, ha='center', color=color)

# Set the plot limits and labels
ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)
ax.set_zlim(-1, 1)
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')
ax.set_title('Solar System')
ax.legend()

# Remove ticks and spines
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Define the data for the planets
planets = {
    "Mercury": {"distance": 0.39, "radius": 0.038, "color": "gray"},
    "Venus": {"distance": 0.72, "radius": 0.095, "color": "bisque"},
    "Earth": {"distance": 1, "radius": 0.1, "color": "mediumturquoise"},
    "Mars": {"distance": 1.52, "radius": 0.053, "color": "indianred"},
    "Jupiter": {"distance": 5.20, "radius": 1.12, "color": "burlywood"},
    "Saturn": {"distance": 9.58, "radius": 0.945, "color": "khaki"},
    "Uranus": {"distance": 19.18, "radius": 0.401, "color": "lightskyblue"},
    "Neptune": {"distance": 30.07, "radius": 0.388, "color": "dodgerblue"}
}

# Create a figure and 3D axis
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Load the galaxy image as a background texture
galaxy_texture = mpimg.imread("C:/Users/patta/AppData/Local/Microsoft/WindowsApps/PY_3_Master/01_Projects/01_01_Project_Alpha/03_Gamma/galaxy.jpg")
galaxy_texture = galaxy_texture / 255.0  # Normalize the image array
ax.plot_surface([-35, 35], [-35, 35], [0, 0], rstride=1, cstride=1, facecolors=galaxy_texture, shade=False)

# Plot the Sun
ax.scatter(0, 0, 0, color='yellow', s=500, label="Sun")

# Plot the orbits and planets
for planet, data in planets.items():
    distance = data["distance"]
    radius = data["radius"]
    color = data["color"]
    theta = np.linspace(0, 2 * np.pi, 100)
    x = distance * np.cos(theta)
    y = distance * np.sin(theta)
    z = np.zeros_like(x)
    ax.plot(x, y, z, color=color)
    ax.scatter(distance, 0, 0, color=color, marker='o', s=100)
    ax.text(distance, 0, 0.05, planet, ha='center', color=color)

# Set the plot limits and labels
ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)
ax.set_zlim(-1, 1)
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')
ax.set_title('Solar System')
ax.legend()

# Remove ticks and spines
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Show the plot
plt.show()


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Define the data for the planets
planets = {
    "Mercury": {"distance": 0.39, "radius": 0.038, "color": "gray"},
    "Venus": {"distance": 0.72, "radius": 0.095, "color": "bisque"},
    "Earth": {"distance": 1, "radius": 0.1, "color": "mediumturquoise"},
    "Mars": {"distance": 1.52, "radius": 0.053, "color": "indianred"},
    "Jupiter": {"distance": 5.20, "radius": 1.12, "color": "burlywood"},
    "Saturn": {"distance": 9.58, "radius": 0.945, "color": "khaki"},
    "Uranus": {"distance": 19.18, "radius": 0.401, "color": "lightskyblue"},
    "Neptune": {"distance": 30.07, "radius": 0.388, "color": "dodgerblue"}
}

# Create a figure and 3D axis
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Load the galaxy image as a background texture
galaxy_texture = mpimg.imread("C:/Users/patta/AppData/Local/Microsoft/WindowsApps/PY_3_Master/01_Projects/01_01_Project_Alpha/03_Gamma/galaxy.jpg")

# Plot the galaxy image as background texture
ax.imshow(galaxy_texture, origin='lower', extent=[-35, 35, -35, 35])

# Plot the Sun
ax.scatter(0, 0, 0, color='yellow', s=500, label="Sun")

# Plot the orbits and planets
for planet, data in planets.items():
    distance = data["distance"]
    radius = data["radius"]
    color = data["color"]
    theta = np.linspace(0, 2 * np.pi, 100)
    x = distance * np.cos(theta)
    y = distance * np.sin(theta)
    z = np.zeros_like(x)
    ax.plot(x, y, z, color=color)
    ax.scatter(distance, 0, 0, color=color, marker='o', s=100)
    ax.text(distance, 0, 0.05, planet, ha='center', color=color)

# Set the plot limits and labels
ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)
ax.set_zlim(-1, 1)
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')
ax.set_title('Solar System')
ax.legend()

# Remove ticks and spines
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Show the plot
plt.show()
