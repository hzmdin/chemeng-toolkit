import numpy as np

def solve_mass_balance(A_matrix, b_vector):
    x = np.linalg.solve(A_matrix, b_vector).flatten()
    for i,x_val in enumerate(x):
        print(f"x{i+1}: {x[i]}")
    if any(x <= 0):
        print(f"Invalid x: {x[x <= 0]}")
        raise Warning("Unphysical negative flow rates / concentrations detected!")
    else:
        print("Physical Solution Found!")
    return x

A_matrix = np.array([[1.0, 1.0, 0.0],[0.4, 0.1, 0.5],[0.2, 0.8, 0.2]])
b_vector = np.array([[150],[70],[30]])
x = solve_mass_balance(A_matrix, b_vector)
print("x")