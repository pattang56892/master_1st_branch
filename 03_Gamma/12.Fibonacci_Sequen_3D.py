import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to generate Fibonacci sequence
def fibonacci(n):
    sequence = [0, 1]  # Initial values
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

# Generate Fibonacci sequence
n = 100  # Number of Fibonacci numbers to generate
fib_seq = fibonacci(n)

# Create data points for the 3D plot
theta = np.linspace(0, 2 * np.pi, n)
z = np.array(fib_seq, dtype=float)  # Convert to float type

# Calculate x and y coordinates using polar coordinates
r = np.sqrt(z)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D line
ax.plot(x, y, z, color='skyblue')

# Set plot limits and labels
ax.set_xlim(-max(r), max(r))
ax.set_ylim(-max(r), max(r))
ax.set_zlim(min(z), max(z))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Fibonacci Number')
ax.set_title('3D Illustration of Fibonacci Sequence')

# Show the plot
plt.show()
