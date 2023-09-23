import matplotlib.pyplot as plt

# Define the coordinates of the 7-star pattern
star_coordinates = [
    (2, 5),
    (3, 4),
    (4, 6),
    (6, 7),
    (7, 5),
    (8, 3),
    (9, 4)
]

# Extract the x and y coordinates
x = [coord[0] for coord in star_coordinates]
y = [coord[1] for coord in star_coordinates]

# Create a plot
fig, ax = plt.subplots()

# Plot the stars
ax.scatter(x, y, color='black', marker='*', s=200)

# Connect the stars to form the constellation lines
ax.plot(x, y, color='gray', linestyle='--')

# Set the plot limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(2, 8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Ursa Major - Big Dipper')

# Show the plot
plt.show()

