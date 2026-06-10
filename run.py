from config import *
from simulation import run
from visualize import plot_initial, plot_trajectory, plot_force

# Initial visualization
plot_initial(pos0, trap0, a)

# Run simulation
traj, forces, traps = run(
    pos0,
    trap0,
    kappa,
    drive,
    eta,
    dt,
    steps
)

# After shear
plot_trajectory(traj, particle=0)
plot_force(forces, particle=0)