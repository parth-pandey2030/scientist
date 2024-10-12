# This file contians information about the
# fundamental forces of the universe.

import numpy as np
import sympy as sp
from constants import G, hbar, c, vacuum_permittivity, vaccuum_permeability, t

# Electromagnetic forces
gauss = lambda electric_charge_density: electric_charge_density / vacuum_permittivity
gauss_magnetism = 0
faraday = lambda magnetic_field: -sp.diff(magnetic_field, t)
ampere_maxwell = lambda electric_field, current_density: vaccuum_permeability * (current_density + vacuum_permittivity * sp.diff(electric_field, t))

# Strong/Weak forces
