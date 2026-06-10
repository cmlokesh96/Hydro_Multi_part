import numpy as np

def trap_force(pos, traps, kappa):
    return -kappa[:, None] * (pos - traps)


def total_force(pos, traps, kappa):
    return trap_force(pos, traps, kappa)