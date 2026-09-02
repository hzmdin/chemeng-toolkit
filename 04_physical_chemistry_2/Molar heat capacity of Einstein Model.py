import numpy as np
import matplotlib.pyplot as plt

def calc_einstein_heat_capacity(T, theta_E):
    R = 8.314
    x = theta_E / T
    C_V = 3 * R * (x**2) * np.exp(-x) / (1-np.exp(-x))**2
    return C_V

# --------------------- MAIN --------------------------
T = np.linspace(10, 1000)
theta_E = 1320
C_V= calc_einstein_heat_capacity(T, theta_E)
plt.plot(T, C_V)
plt.title("Heat Capacity against T")
plt.ylabel("Heat Capacity, C_V")
plt.xlabel("Temperature, T")
plt.show()