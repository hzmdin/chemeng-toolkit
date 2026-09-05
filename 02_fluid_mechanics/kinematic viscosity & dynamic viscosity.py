import numpy as np
import matplotlib.pyplot as plt

def calc_kinematic_viscosity(dyn_visc, density):
    if density <= 0:
        raise ValueError("The density must be positive!")
    if np.any(dyn_visc < 0):
        raise ValueError("The viscosity cannot be negative!")

    kinematic_viscosity = dyn_visc / density
    return kinematic_viscosity

def calc_arrhenius_viscosity(temp_arr, a_const, Ea):
    temp_arr = np.asarray(temp_K)
    if np.any(temp_arr <= 0):
        raise ValueError("Non-physical absolute temperature")
    if Ea <= 0:
        raise ValueError("Activation Energy should be positive.")
    R = 8.314
    mu = a_const*np.exp(Ea / (R*temp_K))
    return mu

############################ MAIN ################################
temp_K = np.linspace(273.15, 383.15, 100)
a_const = 2.414 * 10**-5
Ea = 4789
dyn_visc = calc_arrhenius_viscosity(temp_K, a_const, Ea)
print(f"Arrhenius viscosity: {dyn_visc}")
density = 998.2
kinematic_viscosity = calc_kinematic_viscosity(dyn_visc, density)
print(f"Kinematic Viscosity: {kinematic_viscosity}")

plt.plot(temp_K, kinematic_viscosity, color="blue", label="Trend Line")
plt.xlabel("Temperature (K)")
plt.ylabel("Kinematic viscosity (m²/s)")
plt.title("Temperature (K) against Kinematic Viscosity (m²/s)")
plt.grid(True)
plt.legend()
plt.show()