import matplotlib.pyplot as plt

# Define the data for the planets
planets = {
    "Mercury": {"distance": 0.39, "radius": 0.38},
    "Venus": {"distance": 0.72, "radius": 0.95},
    "Earth": {"distance": 1, "radius": 1},
    "Mars": {"distance": 1.52, "radius": 0.53},
    "Jupiter": {"distance": 5.20, "radius": 11.2},
    "Saturn": {"distance": 9.58, "radius": 9.45},
    "Uranus": {"distance": 19.18, "radius": 4.01},
    "Neptune": {"distance": 30.07, "radius": 3.88}
}

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the planets
for planet, data in planets.items():
    distance = data["distance"]
    radius = data["radius"]
    ax.scatter(distance, 0, color='gray', marker='o')
    ax.annotate(planet, (distance, 0), textcoords="offset points", xytext=(0,10), ha='center')

# Set the plot limits and labels
ax.set_xlim(0, 35)
ax.set_ylim(-15, 15)
ax.set_xlabel('Distance (AU)')
ax.set_title('Solar System - Planets')

# Show the plot
plt.show()
