using Plots

function make(field, behavior)

# Generate X and Y coordinates
x = y = [i for i in field]

# Generate Z values for the surface
z = [behavior(xi, yi) for xi in x, yi in y]

# Plot the surface
surface(x, y, z, xlabel="X", ylabel="Y", zlabel="Z", title="2D Surface Plot") 

end

# Test 
function behavior(x, y)
    return sin(sqrt(x^2 + y^2))
end

field = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

make(field, behavior)