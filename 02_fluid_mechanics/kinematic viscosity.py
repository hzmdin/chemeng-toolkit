def calc_kinematic_viscosity(dyn_visc, density):
    if density <= 0:
        raise ValueError("The density must be positive!")
    if dyn_visc < 0:
        raise ValueError("The viscosity cannot be negative!")

    kinematic_viscosity = dyn_visc / density
    return kinematic_viscosity

dyn_visc = 0.001002
density = 998.2
kinematic_viscosity = calc_kinematic_viscosity(dyn_visc, density)
print(f"Kinematic Viscosity: {kinematic_viscosity}")