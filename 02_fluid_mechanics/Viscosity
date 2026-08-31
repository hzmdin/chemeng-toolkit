import sympy as sp

def calc_macroscopic_stress(F, A):
    return F/A

def calc_viscous_stress_symbolic(mu, u, y_symbol, y_val):
    velocity_gradient = sp.diff(u, y_symbol)
    tau_symbolic = mu*velocity_gradient
    tau_numerical = tau_symbolic.subs(y_symbol, y_val)
    return tau_numerical

y = sp.Symbol('y')
u = 50*y**2
F = 1.2
A = 0.08
mu = 3.5 * 10**-5
y_val = 0.02

print(calc_macroscopic_stress(F,A))
print(calc_viscous_stress_symbolic(mu, u, y, y_val))