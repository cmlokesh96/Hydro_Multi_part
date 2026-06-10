import numpy as np

from forces import trap_force
from hydrodynamics import mobility_matrix
from driving import update_traps
from integrator import step
from simulation import run


# =====================================================
# TEST 1 : Trap Force
# =====================================================

def test_trap_force():

    print("\n[TEST 1] Trap Force")

    pos = np.array([[1.0, 0.0]])
    traps = np.array([[0.0, 0.0]])
    kappa = np.array([2.0])

    F = trap_force(pos, traps, kappa)

    expected = np.array([[-2.0, 0.0]])

    assert np.allclose(F, expected)

    print("PASS")
    print("Force =", F)


# =====================================================
# TEST 2 : Mobility Matrix
# =====================================================

def test_mobility():

    print("\n[TEST 2] Mobility Matrix")

    pos = np.array([
        [0.0, 0.0],
        [10.0, 0.0]
    ])

    H = mobility_matrix(pos, eta=1.0)

    assert H.shape == (4, 4)

    assert np.allclose(H, H.T)

    print(H)
    print("PASS")
    print("Shape =", H.shape)

    print("\nEigenvalues of H:")
    print(np.linalg.eigvals(H))


# =====================================================
# TEST 3 : Oscillating Trap
# =====================================================

def test_driving():

    print("\n[TEST 3] Driving")

    trap0 = np.array([
        [0.0, 0.0],
        [5.0, 0.0]
    ])

    drive = {
        0: {
            "A": 2.0,
            "omega": 1.0,
            "direction": np.array([1.0, 0.0])
        }
    }

    t = np.pi / 2

    traps = update_traps(trap0, drive, t)

    print("Trap positions:")
    print(traps)

    expected_x = 2.0

    assert np.isclose(traps[0, 0], expected_x)

    print("PASS")


# =====================================================
# TEST 4 : One Integration Step
# =====================================================

def test_step():

    print("\n[TEST 4] Single Step")

    pos = np.array([
        [0.2, 0.0]
    ])

    traps = np.array([
        [0.0, 0.0]
    ])

    kappa = np.array([1.0])

    eta = 1.0

    dt = 1e-3

    new_pos, F = step(
        pos,
        traps,
        kappa,
        eta,
        dt
    )

    assert new_pos.shape == pos.shape

    assert F.shape == pos.shape

    print("PASS")
    print("Old position:", pos)
    print("New position:", new_pos)


# =====================================================
# TEST 5 : Short Simulation
# =====================================================

def test_simulation():

    print("\n[TEST 5] Simulation")

    pos0 = np.array([
        [0.0, 0.0],
        [5.0, 0.0]
    ])

    trap0 = pos0.copy()

    kappa = np.ones(2)

    drive = {}

    traj, forces, traps = run(
        pos0=pos0,
        trap0=trap0,
        kappa=kappa,
        drive=drive,
        eta=1.0,
        dt=1e-3,
        steps=100
    )

    assert traj.shape == (100, 2, 2)

    assert forces.shape == (100, 2, 2)

    print("PASS")
    print("Trajectory shape =", traj.shape)


# =====================================================
# TEST 6 : Equilibrium Covariance
# =====================================================

def test_covariance():

    print("\n[TEST 6] Equilibrium Covariance")

    pos0 = np.array([
        [0.0, 0.0],
        [5.0, 0.0]
    ])

    trap0 = pos0.copy()

    kappa = np.ones(2)

    drive = {}

    traj, _, _ = run(
        pos0=pos0,
        trap0=trap0,
        kappa=kappa,
        drive=drive,
        eta=1.0,
        dt=1e-3,
        steps=80000
    )

    fluctuations = traj - trap0

    fluctuations = fluctuations.reshape(
        fluctuations.shape[0],
        -1
    )

    C = np.cov(fluctuations.T)

    print("Covariance Matrix:\n")
    print(C)

    diagonal = np.diag(np.diag(C))

    offdiag_norm = np.linalg.norm(C - diagonal)

    print("\nOff-diagonal norm =", offdiag_norm)

    print("PASS (visual inspection)")


# =====================================================
# RUNNER
# =====================================================

def run_all_tests():

    print("\n===================================")
    print("RUNNING TEST SUITE")
    print("===================================")

    test_trap_force()
    test_mobility()
    test_driving()
    test_step()
    test_simulation()
    test_covariance()

    print("\n===================================")
    print("ALL TESTS COMPLETED")
    print("===================================")


if __name__ == "__main__":
    run_all_tests()