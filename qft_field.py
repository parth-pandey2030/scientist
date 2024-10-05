import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Set up the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the grid for the surface
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)

# Initialize the Z data
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create the surface plot
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# Set labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Animation update function
def update(frame):
    ax.clear()  # Clear the current axis
    Z = np.sin(np.sqrt(X**2 + Y**2) + frame / 10.0)  # Update the Z data
    ax.plot_surface(X, Y, Z, cmap='viridis')  # Re-draw the surface
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

# Create an animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=100)

# Show the plot
plt.show()