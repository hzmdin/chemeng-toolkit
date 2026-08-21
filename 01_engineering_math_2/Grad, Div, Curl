import sympy as sp
from sympy.vector import CoordSys3D, divergence, curl, gradient
import pandas as pd

def calc_grad(scalar_field):
    return gradient(scalar_field)

def calc_divergence(vector_field):
    return divergence(vector_field)

def calc_curl(vector_field):
    return curl(vector_field)

def input_coeff(local_dict):
    u = sp.sympify(input("Please input u value:\n"), locals = local_dict)
    v = sp.sympify(input("Please input v value:\n"), locals = local_dict)
    w = sp.sympify(input("Please input w value:\n"), locals = local_dict)
    return u, v, w

N = CoordSys3D('N')
x, y, z = N.x, N.y, N.z

local_vars = {'x': x, 'y': y, 'z': z}

u, v, w = input_coeff(local_vars)

T = 100* sp.exp(-(x**2 + y**2 + z**2)) # Change the function here
vector_field = u*N.i + v*N.j + w*N.k

grad = calc_grad(T)
div = calc_divergence(vector_field)
cur = calc_curl(vector_field)

print(f"Gradient is {grad}\n")
print(f"divergence is {div}\n")
print(f"curl is {cur}\n")