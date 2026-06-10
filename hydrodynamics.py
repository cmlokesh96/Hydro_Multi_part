import numpy as np
from Sim_Parameters import *

def oseen_tensor_2d(rij, eta):
    r = np.linalg.norm(rij)
    if r < 1e-12:
        return np.zeros((2, 2))

    I = np.eye(2)
    rr = np.outer(rij, rij)

    return (1 / (8 * np.pi * eta * r)) * (I + rr / (r**2))


def mobility_matrix(pos, eta):
    N = len(pos)
    H = np.zeros((2*N, 2*N))

    for i in range(N):
        for j in range(N):

            ri = pos[i]
            rj = pos[j]

            if i == j:
                H[2*i:2*i+2, 2*i:2*i+2] = (1/(6 * np.pi * eta * a))*np.eye(2)  # self mobility 
            else:
                rij = ri - rj
                Hij = oseen_tensor_2d(rij, eta)
                H[2*i:2*i+2, 2*j:2*j+2] = Hij

    return H # np.eye(2*N) /(6 * np.pi * eta * a) 