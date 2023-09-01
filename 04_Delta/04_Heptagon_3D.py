import numpy as np
import matplotlib.pyplot as plt

# Define the center and radius of the circle
center = (0, 0)
radius = 1

# Generate the angles for each vertex of the pentagon
angles = np.linspace(0, 2*np.pi, 6)[:-1]

# Calculate the coordinates of the pentagon vertices
vertices = np.array([(center[0] + radius*np.cos(angle), center[1] + radius*np.sin(angle)) for angle in angles])

# Plot the pentagon vertices
plt.scatter(vertices[:, 0], vertices[:, 1], color='red')

# Connect the vertices with dotted lines
for i in range(5):
    plt.plot([vertices[i, 0], vertices[(i+1)%5, 0]],
             [vertices[i, 1], vertices[(i+1)%5, 1]], '--', color='blue')

# Connect the tips of the vertices to form a big circle
plt.plot(vertices[:, 0], vertices[:, 1], '--', color='green')

# Connect the adjacent points to form a perfect star
plt.plot([vertices[0, 0], vertices[2, 0]], [vertices[0, 1], vertices[2, 1]], '--', color='purple')
plt.plot([vertices[1, 0], vertices[3, 0]], [vertices[1, 1], vertices[3, 1]], '--', color='purple')
plt.plot([vertices[2, 0], vertices[4, 0]], [vertices[2, 1], vertices[4, 1]], '--', color='purple')
plt.plot([vertices[3, 0], vertices[0, 0]], [vertices[3, 1], vertices[0, 1]], '--', color='purple')
plt.plot([vertices[4, 0], vertices[1, 0]], [vertices[4, 1], vertices[1, 1]], '--', color='purple')

# Set the x-axis and y-axis scales
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

# Set the x-axis and y-axis labels
plt.xlabel('X')
plt.ylabel('Y')

# Set the plot title
plt.title('Regular Pentagon Star Visualization')

# Show the plot
plt.show()



