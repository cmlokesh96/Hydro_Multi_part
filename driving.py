import numpy as np

def update_traps(trap0, drive, t):
    traps = trap0.copy()

    for i, d in drive.items():
        disp = d["A"] * np.sin(d["omega"] * t) * d["direction"]
        traps[i] += disp

    return traps