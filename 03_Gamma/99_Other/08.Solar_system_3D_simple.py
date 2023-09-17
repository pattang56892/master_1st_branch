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

# Set the background color of the 3D plot
ax.w_xaxis.set_pane_color((0, 0, 0, 0))
ax.w_yaxis.set_pane_color((0, 0, 0, 0))
ax.w_zaxis.set_pane_color((0, 0, 0, 0))

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


