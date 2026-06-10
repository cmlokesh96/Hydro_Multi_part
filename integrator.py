import numpy as np
from hydrodynamics import mobility_matrix
from forces import total_force
from Sim_Parameters import kBT

def step(pos, traps, kappa, eta, dt):

    F = total_force(pos, traps, kappa)

    H = mobility_matrix(pos, eta)

    D = kBT * H

    A = np.linalg.cholesky(D + 1e-20*np.eye(len(D)))

    N = len(pos)

    R = np.random.normal(0, 1, 2*N) 

    drift = dt * (H @ F.flatten())

    noise = np.sqrt(2 * dt) * (A @ R)

    new_pos = pos.flatten() + drift + noise

    return new_pos.reshape(N, 2), F