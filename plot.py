import matplotlib.pyplot as plt
import numpy as np


inf = 100
n_range = np.arange(-inf, inf + 1)
epsilon = 1e-10


def delta(x):
    if abs(x) < epsilon:
        return 1
    else:
        return 0


def x_s(t_range: np.ndarray, omega_m):
    res = []
    for t in t_range:
        y = 0
        for n in n_range:
            y += np.cos(omega_m * t) * delta(t - 2 * n * np.pi)
        res.append(y)
    return res


def X_j(omega_m, omega_arr):
    res = []
    for omega in omega_arr:
        y = 0
        for n in n_range:
            y += delta(omega - omega_m - n) + delta(omega + omega_m - n)
        res.append(y / 2)
    return np.array(res)


if __name__ == "__main__":
    omega_m = 9 / 8
    n = 5
    step = 2 * np.pi / 800
    t_range = np.arange(-n * 2 * np.pi, n * 2 * np.pi + step, step)
    omega_range = np.arange(- n - 1, n + 1, 1 / 1024)
    x_s_arr = x_s(t_range, omega_m)
    X_j_arr = X_j(omega_m, omega_range)
    fig = plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(t_range, x_s_arr)
    plt.xlabel('t')
    plt.ylabel('x_s(t)')
    plt.title("x_s(t) - t Curve")
    plt.subplot(2, 1, 2)
    plt.plot(omega_range, X_j_arr)
    plt.xlabel('omega')
    plt.ylabel('X_s(j omega)')
    plt.title("X_s(j omega) - omega Curve")
    plt.show()
