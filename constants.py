from math import sqrt
from sympy import symbols
import numpy as np

__all__ = [
    'pi',
    'e',
    'i',
    'phi',
    'golden',
    'golden_ratio',
    'meter',
    'm',
    'second',
    's',
    'kilogram',
    'kg',
    'newton',
    'N',
    'kelvin',
    'K',
    'candela',
    'cd',
    'hbar_unit',
    'PLANCK_CONSTANT_UNIT',
    'c_unit',
    'SPEED_OF_LIGHT_UNIT',
    'quetta',
    'ronna',
    'yotta',
    'zetta',
    'exa',
    'peta',
    'tera',
    'giga',
    'mega',
    'kilo',
    'hecto',
    'deka',
    'deci',
    'centi',
    'milli',
    'micro',
    'nano',
    'pico',
    'femto',
    'atto',
    'zepto',
    'yocto',
    'ronto',
    'quecto'
    'minute',
    'hour',
    'day',
    'year',
    'parsec',
    'observable_universe_radius',
    'c',
    'SPEED_OF_LIGHT',
    'h',
    'PLANCK_CONSTANT',
    'hbar',
    'REDUCED_PLANCK_CONSTANT',
    'k',
    'BOLTZMANN_CONSTANT',
    'G',
    'NEWTON_CONSTANT',
    'eV',
    'vacuum_permittivity',
    'alpha',
    'FINE_STRUCTURE_CONSTANT',
    'H',
    'HUBBLE_CONSTANT',
    'lp',
    'PLANCK_LENGTH',
    'tp',
    'PLANCK_TIME',
    'mp',
    'PLANCK_MASS',
    'ep',
    'PLANCK ENERGY',
    'Tp',
    'PLANCK_TEMPERATURE',
    'qp',
    'PLANCK_ENERGY',
    'Λ',
    'COSMOLOGICAL_CONSTANT',
    't'
]

# Mathematical constants
pi = 3.14159265358979323846;
e = 2.712845904523536;
i = 1j
phi = golden = golden_ratio = (1 + sqrt(5)) / 2

# Units
meter = m = second = s = kilogram = kg = newton = N = kelvin = K = candela = cd = hbar_unit = PLANCK_CONSTANT_UNIT = c_unit = SPEED_OF_LIGHT_UNIT = 1

# Prefixes
quetta = 1e30
ronna = 1e27
yotta = 1e24
zetta = 1e21
exa = 1e18
peta = 1e15
tera = 1e12
giga = 1e9
mega = 1e6
kilo = 1e3
hecto = 1e2
deka = 1e1
deci = 1e-1
centi = 1e-2
milli = 1e-3
micro = 1e-6
nano = 1e-9
pico = 1e-12
femto = 1e-15
atto = 1e-18
zepto = 1e-21
yocto = 1e-24
ronto = 1e-27
quecto = 1e-30

# Time and Length
minute = 60
hour = 3600
day = 24 * hour
week = 7 * day
month = 30 * day
year = 365.25 * day
km = 1000
mile = 1609.344
au = 149597870700
light_year = 9460730472580800
parsec = 3.08567758128e16
observable_universe_radius = 45.5 * giga * light_year

# Physical constants
c = SPEED_OF_LIGHT = 2.9979245
h = PLANCK_CONSTANT = 6.62606957e-3
hbar = REDUCED_PLANCK_CONSTANT = 1.0545718e-3
k = BOLTZMANN_CONSTANT = 1.3806488e-2
G = NEWTON_CONSTANT = 6.67384e-1
eV = electron_volt = elementary_charge = 1.60217662e-1
vacuum_permittivity = 8.854187817e-12
vaccuum_permeability = 1.25663706127(20) * micro
alpha = FINE_STRUCURE_CONSTANT =elementary_charge ** 2 / (4 * pi * vacuum_permittivity * hbar * c)
H = HUBBLE_CONSTANT = 74 * km / s / (mega * parsec)

# Structure Constants
def structure_constant(a, b, c):
    global gell_mann_matrices
    global generator 

    gell_mann_matrices = {
        '1': np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        '2': np.array([[0, -i, 0], [i, 0, 0], [0, 0, 0]]),
        '3': np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
        '4': np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        '5': np.array([[0, 0, -i], [0, 0, 0], [i, 0, 0]]),
        '6': np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
        '7': np.array([[0, 0, 0], [0, 0, -i], [0, i, 0]]),
        '8': 1/sqrt(3) * np.array([[1, 0, 0], [1, 0, 0], [0, 0, -2]]),
    }
    generator = lambda x: 1/2 * gell_mann_matrices[x]

    return [generator(a), generator(b)] / (i * generator(c))
    
# Planck units
lp = PLANCK_LENGTH = sqrt((hbar * G) / c ** 3)
tp = PLANCK_TIME = PLANCK_LENGTH / c 
mp = PLANCK_MASS = sqrt((hbar * c) / G)
ep = PLANCK_ENERGY = mp * c ** 2
Tp = PLANCK_TEMPERATURE = PLANCK_ENERGY / k
qp = PLANCK_CHARGE = sqrt(4 * pi * vacuum_permittivity * hbar * c)

# Other     
Λ = COSMOLOGICAL_CONSTANT = lp ** -2 * 10e-122
t = symbols('t')    