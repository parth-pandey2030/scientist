from scipy.constants import angstrom
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to create and display a 3D field (surface plot)
def make_field(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create the surface plot
    ax.plot_surface(x, y, z, color='b', alpha=0.6)  # Semi-transparent blue surface
    
    # Set labels and title
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('Electron Cloud of Hydrogen Atom')

    # Set limits to focus on the region around the atom
    ax.set_xlim([-1, 1])  # Adjust based on the radius
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    # Show the plot
    plt.show()

# Define the behavior for hydrogen atom's electron cloud
def hydrogen_behavior():
    # Define the Bohr radius
    radius = 0.529 * angstrom

    # Create a meshgrid in spherical coordinates
    theta = np.linspace(0, np.pi, 100)  # Polar angle (from 0 to pi)
    phi = np.linspace(0, 2 * np.pi, 100)  # Azimuthal angle (from 0 to 2pi)
    theta, phi = np.meshgrid(theta, phi)

    # Convert spherical coordinates to Cartesian coordinates
    x = radius * np.sin(theta) * np.cos(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(theta)
    
    return x, y, z

# Main function to plot the hydrogen atom surface
if __name__ == '__main__':
    x, y, z = hydrogen_behavior()
    make_field(x, y, z)

