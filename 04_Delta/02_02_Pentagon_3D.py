import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import mplcursors

# Define the center and radius of the circle
center = (0, 0, 0)
radius = 1

# Generate the angles for each vertex of the pentagon
angles = np.linspace(0, 2*np.pi, 6)[:-1]

# Calculate the coordinates of the pentagon vertices
vertices = np.array([(center[0] + radius*np.cos(angle), center[1] + radius*np.sin(angle), center[2]) for angle in angles])

# Create the figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the pentagon
polygon = Poly3DCollection([vertices], alpha=0.25, linewidths=1, edgecolors='black', facecolors='blue')
ax.add_collection3d(polygon)

# Plot the edges of the pentagon
edges = Line3DCollection([(vertices[i], vertices[(i+1)%5]) for i in range(5)], linewidths=1, colors='black')
ax.add_collection3d(edges)

# Enable interactive labels
mplcursors.cursor(hover=True)

# Function to update the pentagon vertices when dragging
def update_vertices(event):
    if event.artist == polygon:
        # Get the new center coordinates
        new_center = event.artist.get_center()
        
        # Calculate the new vertices
        new_vertices = np.array([(new_center[0] + radius*np.cos(angle), new_center[1] + radius*np.sin(angle), new_center[2]) for angle in angles])
        
        # Update the polygon
        polygon.set_verts([new_vertices])
        
        # Update the edges
        edges.set_segments([(new_vertices[i], new_vertices[(i+1)%5]) for i in range(5)])
        
        # Redraw the figure
        fig.canvas.draw()

# Connect the update_vertices function to the motion_notify_event
fig.canvas.mpl_connect('motion_notify_event', update_vertices)

# Set the plot limits
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

# Set the labels for each axis
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()


import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# Define the center and radius of the circle
center = (0, 0)
radius = 1

# Generate the angles for each vertex of the pentagon
angles = np.linspace(0, 2*np.pi, 6)[:-1]

# Calculate the coordinates of the pentagon vertices
vertices = np.array([(center[0] + radius*np.cos(angle), center[1] + radius*np.sin(angle)) for angle in angles])

# Create the figure and axes
fig, ax = plt.subplots()

# Plot the pentagon vertices
ax.scatter(vertices[:, 0], vertices[:, 1], color='blue')

# Plot the spheres at each tip of the pentagon
for vertex in vertices:
    ax.add_patch(plt.Circle(vertex, 0.1, color='red', alpha=0.25))

# Plot the lines connecting the vertices
for i in range(5):
    ax.plot([vertices[i, 0], vertices[(i+2)%5, 0]], [vertices[i, 1], vertices[(i+2)%5, 1]], linestyle='dotted', color='black')

# Set the aspect ratio to equal
ax.set_aspect('equal')

# Set the plot limits
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Set the labels for each axis
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Show the plot
plt.show()


import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# Define the center and radius of the circle
center = (0, 0)
radius = 1

# Generate the angles for each vertex of the pentagon
angles = np.linspace(0, 2*np.pi, 6)[:-1]

# Calculate the coordinates of the pentagon vertices
vertices = np.array([(center[0] + radius*np.cos(angle), center[1] + radius*np.sin(angle)) for angle in angles])

# Create the figure and axes
fig, ax = plt.subplots()

# Plot the pentagon vertices
ax.scatter(vertices[:, 0], vertices[:, 1], color='blue')

# Plot the spheres at each tip of the pentagon
for vertex in vertices:
    ax.add_patch(plt.Circle(vertex, 0.1, color='red', alpha=0.25))
    ax.plot([vertex[0]], [vertex[1]], 'ro')

# Plot the lines connecting the vertices
for i in range(5):
    ax.plot([vertices[i, 0], vertices[(i+1)%5, 0]], [vertices[i, 1], vertices[(i+1)%5, 1]], linestyle='dotted', color='black')
    ax.plot([vertices[i, 0], vertices[(i+2)%5, 0]], [vertices[i, 1], vertices[(i+2)%5, 1]], linestyle='dotted', color='black')

# Set the aspect ratio to equal
ax.set_aspect('equal')

# Set the plot limits
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Set the labels for each axis
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Show the plot
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import mplcursors

# Define the center and radius of the circle
center = (0, 0, 0)
radius = 1

# Generate the angles for each vertex of the pentagon
angles = np.linspace(0, 2*np.pi, 6)[:-1]

# Calculate the coordinates of the pentagon vertices
vertices = np.array([(center[0] + radius*np.cos(angle), center[1] + radius*np.sin(angle), center[2]) for angle in angles])

# Create the figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the pentagon
polygon = Poly3DCollection([vertices], alpha=0.25, linewidths=1, edgecolors='black', facecolors='blue')
ax.add_collection3d(polygon)

# Plot the edges of the pentagon
edges = Line3DCollection([(vertices[i], vertices[(i+1)%5]) for i in range(5)], linewidths=1, colors='black')
ax.add_collection3d(edges)

# Enable interactive labels
mplcursors.cursor(hover=True)

# Function to update the pentagon vertices when dragging
def update_vertices(event):
    if event.artist == polygon:
        # Get the new center coordinates
        new_center = event.artist.get_center()
        
        # Calculate the new vertices
        new_vertices = np.array([(new_center[0] + radius*np.cos(angle), new_center[1] + radius*np.sin(angle), new_center[2]) for angle in angles])
        
        # Update the polygon
        polygon.set_verts([new_vertices])
        
        # Update the edges
        edges.set_segments([(new_vertices[i], new_vertices[(i+1)%5]) for i in range(5)])
        
        # Redraw the figure
        fig.canvas.draw()

# Connect the update_vertices function to the motion_notify_event
fig.canvas.mpl_connect('motion_notify_event', update_vertices)

# Set the plot limits
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

# Set the labels for each axis
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
