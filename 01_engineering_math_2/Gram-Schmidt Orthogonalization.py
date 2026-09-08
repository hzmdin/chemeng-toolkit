import numpy as np
import matplotlib.pyplot as plt

def proj(v, u):
    return ((v @ u) / (u @ u))*u

def gram_schmidt_3d(v1, v2, v3):
    u1 = v1
    u2 = v2 - proj(v2, u1)
    u3 = v3 - proj(v3, u1) - proj(v3, u2)

    e1 = u1 / np.linalg.norm(u1)
    e2 = u2 / np.linalg.norm(u2)
    e3 = u3 / np.linalg.norm(u3)

    if (abs(e1 @ e2) < 1e-7) and (abs(e1 @ e3) < 1e-7):
        return e1, e2, e3
    else:
        raise ValueError("The unit vector is not orthogonal to each other")

v1 = np.array([3.0, 17.0, 0.0])
v2 = np.array([7.0, 2.0, 0.0])
v3 = np.array([1.0, 1.0, 16.0])
e_arr = gram_schmidt_3d(v1, v2, v3)
e1, e2, e3 = e_arr[0], e_arr[1], e_arr[2]

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.quiver(0, 0, 0, e1, e2, e3)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
plt.show()