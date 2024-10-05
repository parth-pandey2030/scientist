import numpy as np
import matplotlib.pyplot as plt
import math

def generate_field(behavior: function, value: np.ndarray = 0, is_local = False) -> np.ndarray:
    """
    # Field Generator

    Fields are mathematical fluids that encompass either a local volume 
    or all space.
    """
    field = []
    finite = False
    if is_local:
        finite = True
    
    if finite:
        if type(value) == np.ndarray:
            for val in value:
                field.append(behavior(val))
        else:
            field.append(behavior(value))
    else:
        field = behavior(value)
    
    return np.array(field)

# Test field
def behavior(x):
    return np.sin(x)

field = generate_field(behavior, 0, True)
print(field)