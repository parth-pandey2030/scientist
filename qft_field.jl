using Plots

# Generate X and Y coordinates
x = range(-5, 5, length=50)
y = range(-5, 5, length=50)

# Generate Z values for the surface
z = [sin(sqrt(xi^2 + yi^2)) for xi in x, yi in y]

# Plot the surface
surface(x, y, z, xlabel="X", ylabel="Y", zlabel="Z", title="2D Surface Plot")