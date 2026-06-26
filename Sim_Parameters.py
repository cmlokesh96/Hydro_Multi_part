import numpy as np
from Trap_Initilize import initialize_traps
# Physical params
kBT = 1.38e-23 * (273 + 25)
a = 3e-6
eta = 0.05e-6 / (6 * np.pi * a )


# Simulation
dt = 5e-4
steps = 100000

# System
N = 3


separation_factor = 3
# Trap stiffness
KT = 2e-6
kappa = np.ones(N) * KT

# Initial trap centers (fixed lattice)
trap0 = initialize_traps(N, a, separation_factor=separation_factor)

# Initial positions
# The standard deviation of the particle's position at thermal equilibrium is sqrt(kBT/kappa)
pos0 = trap0 + np.sqrt(kBT / KT) * np.random.randn(N, 2)   

R = separation_factor * a

omega=1*2*np.pi 

# Driving
drive = {
    1: {"A": R/2, "omega": omega, "direction": np.array([1.0, 0.0])}
}