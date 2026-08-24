import numpy as np
import matplotlib.pyplot as plt

def evaluate_3d_line_vectorized(r0, v, t_array):
    r0_array = np.array(r0, dtype= float)
    v_array = np.array(v, dtype = float)
    t_column = t_array[:, np.newaxis]
    r_matrix = r0_array + (t_column*v_array)
    return r_matrix # this is array

def calc_vector_distance(p1, p2):
    delta_p = p2 - p1
    distance = np.linalg.norm(delta_p) # np.linalg.norm() calculates the magnitude / length / distance of a vector or matrix
    return distance

# Main Execution
r0_input = [1.0, 2.0, 0.0]
v_input = [3.0, -1.0, 4.0]

t_array = np.linspace(0.0, 5.0, 100)
trajectory_points = evaluate_3d_line_vectorized(r0_input, v_input, t_array)

start_point = trajectory_points[0]
end_point = trajectory_points[-1]
total_distance = calc_vector_distance(start_point, end_point)
print(f"Total displacement distance: {total_distance}")

# Now creating Visualization with Matplotlib
fig, ax = plt.subplots(subplot_kw={'projection':'3d'})

x_vals = trajectory_points[:, 0]
y_vals = trajectory_points[:, 1]
z_vals = trajectory_points[:, 2]

ax.plot(x_vals, y_vals, z_vals, label='Trajectory')

ax.scatter(start_point[0], start_point[1], start_point[2], label='Initial Position (r0)', color='red')
ax.scatter(end_point[0], end_point[1], end_point[2], label='Final Position', color='green')

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.legend()
plt.show()