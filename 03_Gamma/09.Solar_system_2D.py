import matplotlib.pyplot as plt
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

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={"projection": "polar"})

# Plot the orbits and planets
for planet, data in planets.items():
    distance = data["distance"]
    radius = data["radius"]
    color = data["color"]
    theta = np.linspace(0, 2 * np.pi, 100)
    r = distance * np.ones_like(theta)
    ax.plot(theta, r, color=color, linestyle='dotted')

    # Plot the planet as a point
    ax.scatter(0, distance, color=color, s=100)

    # Add label for the planet
    ax.text(0, distance, planet, ha='center', va='center', color=color)

# Set the plot limits and labels
ax.set_rticks([])
ax.spines['polar'].set_visible(False)
ax.set_yticklabels([])
ax.set_title('Solar System')

plt.show()
