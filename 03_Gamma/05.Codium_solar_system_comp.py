import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Define the data for the planets
planets = {
    "Mercury": {"distance": 0.39, "radius": 0.38, "color": "gray"},
    "Venus": {"distance": 0.72, "radius": 0.95, "color": "bisque"},
    "Earth": {"distance": 1, "radius": 1, "color": "mediumturquoise"},
    "Mars": {"distance": 1.52, "radius": 0.53, "color": "indianred"},
    "Jupiter": {"distance": 5.20, "radius": 11.2, "color": "burlywood"},
    "Saturn": {"distance": 9.58, "radius": 9.45, "color": "khaki"},
    "Uranus": {"distance": 19.18, "radius": 4.01, "color": "lightskyblue"},
    "Neptune": {"distance": 30.07, "radius": 3.88, "color": "dodgerblue"}
}

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Load the galaxy image
galaxy = mpimg.imread("C:/Users/patta/AppData/Local/Microsoft/WindowsApps/PY_3_Master/01_Projects/01_01_Project_Alpha/03_Gamma/galaxy.jpg")

# Plot the background galaxy image
ax.imshow(galaxy, extent=[-35, 35, -35, 35])

# Plot the Sun
ax.scatter(0, 0, color='yellow', s=500, label="Sun")

# Plot the orbits and planets
for planet, data in planets.items():
    distance = data["distance"]
    radius = data["radius"]
    color = data["color"]
    theta = np.linspace(0, 2 * np.pi, 100)
    x = distance * np.cos(theta)
    y = distance * np.sin(theta)
    ax.plot(x, y, color=color)
    ax.scatter(distance, 0, color=color, marker='o', s=100)
    ax.annotate(planet, (distance, 0), textcoords="offset points", xytext=(0, 10), ha='center', color=color)

# Set the plot limits and labels
ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_title('Solar System')
ax.legend()

# Remove ticks and spines
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Show the plot
plt.show()
