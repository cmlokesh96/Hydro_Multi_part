import numpy as np


def initialize_traps(N, a, separation_factor=2.5):
    """Initializes N trap positions as a regular polygon centered at the origin

    with a guaranteed side-length distance R > 2a.

    Parameters:
    -----------
    N : int
        Number of traps (must be >= 2)
    a : float
        Radius of the particle
    separation_factor : float
        Multiplier for 'a' to set the distance R (must be > 2.0)

    Returns:
    --------
    np.ndarray
        Shape (N, 2) array containing the trap coordinates
    """
    if N < 2:
        raise ValueError("Number of particles N must be at least 2.")

    # 1. Define target distance R strictly greater than 2*a
    R = separation_factor * a

    # 2. Handle N=2 explicitly (flat line split on x-axis)
    if N == 2:
        return np.array([[-R / 2, 0.0], [R / 2, 0.0]])

    # 3. For N >= 3, calculate the circumradius to get side length R
    circumradius = R / (2 * np.sin(np.pi / N))

    # 4. Determine an angular offset to keep shapes visually symmetric
    # If N=3, an offset of -pi/6 places the base flat on the x-axis
    if N == 3:
        start_angle = -np.pi / 6
    # For even numbers, rotating by pi/N puts flat edges parallel to axes
    elif N % 2 == 0:
        start_angle = np.pi / N
    else:
        start_angle = 0.0

    # 5. Generate angles uniformly distributed around the circle
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False) + start_angle

    # 6. Compute Cartesian coordinates
    traps = np.zeros((N, 2))
    traps[:, 0] = circumradius * np.cos(angles)  # X coordinates
    traps[:, 1] = circumradius * np.sin(angles)  # Y coordinates

    return traps
