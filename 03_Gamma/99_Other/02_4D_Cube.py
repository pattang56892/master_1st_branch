import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data points for a cube in 3D space
cube_vertices = [
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
]

# Extend the cube to the fourth dimension
fourth_dimension = 0.5
extended_cube_vertices = []
for vertex in cube_vertices:
    extended_vertex = vertex + [fourth_dimension]
    extended_cube_vertices.append(extended_vertex)

# Plot the cube in 4D space
x = [vertex[0] for vertex in extended_cube_vertices]
y = [vertex[1] for vertex in extended_cube_vertices]
z = [vertex[2] for vertex in extended_cube_vertices]
ax.scatter(x, y, z)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('4D Cube')

# Set plot limits
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Show the plot
plt.show()
