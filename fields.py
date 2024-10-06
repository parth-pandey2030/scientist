#%%
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from typing import Callable

def make_field(func: Callable, cmap: str = 'viridis', title: str = 'Surface Plot'):

    # Set up the figure and 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define the grid for the surface
    X = np.linspace(-5, 5, 100)
    Y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(X, Y)

    # Compute Z values from the function
    Z = func(X, Y)

    # Create the surface plot with the selected colormap
    surf = ax.plot_surface(X, Y, Z, cmap=cmap)

    # Set labels and title
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title(title)

    # Add a color bar for reference
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

    # Optionally set a fixed range for better visual effect
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-1.5, 1.5])  # Adjust this based on the expected range of Z

    # Show the plot
    plt.show()

if __name__ == '__main__':
    make_field(lambda x, y: np.sin(np.sqrt(x**2 + y**2)), cmap='plasma', title='Radial Sinusoidal Field')
