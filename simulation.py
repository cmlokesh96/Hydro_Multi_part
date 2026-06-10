import numpy as np
from integrator import step
from driving import update_traps

def run(pos0, trap0, kappa, drive, eta, dt, steps):

    pos = pos0.copy()

    traj = []
    forces = []
    traps_hist = []

    for t in range(steps):

        time = t * dt

        traps = update_traps(trap0, drive, time)

        pos, F = step(pos, traps, kappa, eta, dt)

        traj.append(pos.copy())
        forces.append(F.copy())
        traps_hist.append(traps.copy())

    return np.array(traj), np.array(forces), np.array(traps_hist)