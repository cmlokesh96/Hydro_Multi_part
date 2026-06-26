import numpy as np
import matplotlib.pyplot as plt
from Sim_Parameters import *

def plot_initial(pos, traps, a):
    # Scale all spatial dimensions from meters to micrometers
    pos_um = pos * 1e6
    traps_um = traps * 1e6
    a_um = a * 1e6
    
    fig, ax = plt.subplots(figsize=(6, 6))

    # 1. Plot the center points of the traps
    ax.scatter(
        traps_um[:, 0], traps_um[:, 1], c="red", marker="x", s=80, label="Trap Centers"
    )

    # 2. Plot the center points of the particles
    ax.scatter(
        pos_um[:, 0],
        pos_um[:, 1],
        c="blue",
        marker="o",
        s=20,
        label="Particle Centers",
        zorder=3,
    )

    # Label each particle with its index (0, 1, 2, ...)
    for i, (x, y) in enumerate(pos_um):
        ax.text(x + 0.8, y + 0.8, str(i), fontsize=10, color="black", zorder=4)

    # 3. Add a physical circle of radius 'a_um' around each particle center
    for i in range(len(pos_um)):
        circle = plt.Circle(
            (pos_um[i, 0], pos_um[i, 1]),
            radius=a_um,
            color="blue",
            alpha=0.2,  # Semi-transparent fill
            ec="blue",  # Edge color
            lw=1.5,  # Line width
            zorder=2,
        )
        ax.add_patch(circle)

    # Styling and adjustments
    ax.set_title("Initial Configuration (with particle radius)")
    ax.set_xlabel("X position (μm)")
    ax.set_ylabel("Y position (μm)")
    ax.legend(loc="upper right")
    ax.axis("equal")  # Keeps circles from looking like ellipses

    # Dynamically scale the plot limits in micrometer scale
    all_x = np.concatenate([pos_um[:, 0], traps_um[:, 0]])
    all_y = np.concatenate([pos_um[:, 1], traps_um[:, 1]])
    
    # Pad layout borders by particle radius plus a 10 micrometer safety threshold
    ax.set_xlim(min(all_x) - (a_um + 10), max(all_x) + (a_um + 10))
    ax.set_ylim(min(all_y) - (a_um + 10), max(all_y) + (a_um + 10))

    ax.grid(True, linestyle="--", alpha=0.5)
    plt.show()


def plot_trajectory(traj, dt=dt, particle=0):
    num_steps = len(traj)
    time_axis = np.arange(num_steps) * dt
    
    # Convert chosen particle coordinates to micrometers
    x_coords = traj[:, particle, 0] * 1e6
    y_coords = traj[:, particle, 1] * 1e6

    # Create 2 stacked subplots sharing the same time axis
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

    # X position subplot
    ax1.plot(time_axis, x_coords, label="x", color="tab:blue")
    ax1.set_ylabel("X Position (μm)")
    ax1.set_title(f"Particle {particle} Trajectory Components")
    ax1.grid(True, linestyle="--", alpha=0.5)
    ax1.legend(loc="upper right")

    # Y position subplot
    ax2.plot(time_axis, y_coords, label="y", color="tab:orange")
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Y Position (μm)")
    ax2.grid(True, linestyle="--", alpha=0.5)
    ax2.legend(loc="upper right")

    plt.tight_layout()
    plt.show()


def plot_force(forces, dt=dt, particle=0):
    num_steps = len(forces)
    time_axis = np.arange(num_steps) * dt

    # Extract distinct force components
    fx = forces[:, particle, 0]
    fy = forces[:, particle, 1]

    # Create 2 stacked subplots sharing the same time axis
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

    # Fx subplot
    ax1.plot(time_axis, fx, label="$F_x$", color="tab:green")
    ax1.set_ylabel("Force X")
    ax1.set_title(f"Force Components for Particle {particle}")
    ax1.grid(True, linestyle="--", alpha=0.5)
    ax1.legend(loc="upper right")

    # Fy subplot
    ax2.plot(time_axis, fy, label="$F_y$", color="tab:red")
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Force Y")
    ax2.grid(True, linestyle="--", alpha=0.5)
    ax2.legend(loc="upper right")

    plt.tight_layout()
    plt.show()



# def plot_initial(pos, traps, a):
#     fig, ax = plt.subplots(figsize=(6, 6))

#     # 1. Plot the center points of the traps
#     ax.scatter(
#         traps[:, 0], traps[:, 1], c="red", marker="x", s=80, label="Trap Centers"
#     )

#     # 2. Plot the center points of the particles
#     ax.scatter(
#         pos[:, 0],
#         pos[:, 1],
#         c="blue",
#         marker="o",
#         s=20,
#         label="Particle Centers",
#         zorder=3,
#     )

#     # 3. Add a physical circle of radius 'a' around each particle center
#     # 'a' is imported globally from your config file
#     for i in range(len(pos)):
#         # Create a circle patch
#         circle = plt.Circle(
#             (pos[i, 0], pos[i, 1]),
#             radius=a,
#             color="blue",
#             alpha=0.2,  # Semi-transparent fill
#             ec="blue",  # Edge color
#             lw=1.5,  # Line width
#             zorder=2,
#         )
#         ax.add_patch(circle)

#     # Styling and adjustments
#     ax.set_title("Initial Configuration (with particle radius)")
#     ax.set_xlabel("X position")
#     ax.set_ylabel("Y position")
#     ax.legend(loc="upper right")
#     ax.axis("equal")  # CRITICAL: Keeps circles from looking like ellipses

#     # Dynamically scale the plot limits so the circles aren't cut off
#     all_x = np.concatenate([pos[:, 0], traps[:, 0]])
#     all_y = np.concatenate([pos[:, 1], traps[:, 1]])
#     ax.set_xlim(min(all_x) - (a + 10e-6), max(all_x) + (a + 10e-6))
#     ax.set_ylim(min(all_y) - (a + 10e-6), max(all_y) + (a + 10e-6))

#     ax.grid(True, linestyle="--", alpha=0.5)
#     plt.show()

# def plot_trajectory(traj, dt = dt, particle=0):
#     # Calculate the total number of frames/steps
#     num_steps = len(traj)

#     # Create an array of timestamps: [0, dt, 2*dt, ..., (num_steps-1)*dt]
#     time_axis = np.arange(num_steps) * dt

#     plt.figure()

#     # Plot x  coordinates against the physical time axis
#     plt.plot(time_axis, traj[:, particle, 0]*1e6, label="x")
    

#     plt.xlabel("Time (s)")  # Added axis label
#     plt.ylabel("Position (μm)")
#     plt.legend()
#     plt.title(f"Particle {particle} trajectory")
#     plt.grid(True, linestyle="--", alpha=0.5)
#     plt.show()

#     plt.figure()

#     # Plot y coordinates against the physical time axis
    
#     plt.plot(time_axis, traj[:, particle, 1]*1e6, label="y")

#     plt.xlabel("Time (s)")  # Added axis label
#     plt.ylabel("Position (μm)")
#     plt.legend()
#     plt.title(f"Particle {particle} trajectory")
#     plt.grid(True, linestyle="--", alpha=0.5)
#     plt.show()


# def plot_force(forces, dt = dt, particle=0):
#     num_steps = len(forces)

#     # Create the same physical time axis
#     time_axis = np.arange(num_steps) * dt

#     plt.figure()

#     f = forces[:, particle, :]
#     force_magnitude = np.linalg.norm(f, axis=1)

#     # Plot the magnitude against the physical time axis
#     plt.plot(time_axis, force_magnitude)

#     plt.xlabel("Time (s)")  # Added axis label
#     plt.ylabel("Force Magnitude")
#     plt.title(f"Force magnitude particle {particle}")
#     plt.grid(True, linestyle="--", alpha=0.5)
#     plt.show()


# def plot_initial(pos, traps):

#     plt.figure()
#     plt.scatter(pos[:,0], pos[:,1], label="particles")
#     plt.scatter(traps[:,0], traps[:,1], label="traps")
#     plt.legend()
#     plt.title("Initial configuration")
#     plt.axis("equal")
#     plt.show()


# def plot_trajectory(traj, particle=0):

#     plt.figure()

#     plt.plot(traj[:,particle,0], label="x")
#     plt.plot(traj[:,particle,1], label="y")

#     plt.legend()
#     plt.title(f"Particle {particle} trajectory")
#     plt.show()


# def plot_force(forces, particle=0):

#     plt.figure()

#     f = forces[:,particle,:]

#     plt.plot(np.linalg.norm(f, axis=1))

#     plt.title(f"Force magnitude particle {particle}")
#     plt.show()