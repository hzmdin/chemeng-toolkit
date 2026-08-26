import warnings
import math

def calc_reynolds(rho, v, D, mew):
    if any(param <= 0 for param in (rho, v, D, mew)):
        raise ValueError("The input value is invalid")
    else:
        Re = (rho*v*D)/mew
        return Re

def calc_darcy_friction(Re, epsilon, D, regime):
    if regime.lower() == "laminar":
        f = 64 / Re
        return f
    elif regime.lower() == "turbulent":
        relative_roughness = epsilon / D
        term1_f = relative_roughness / 3.7
        term2_f = 5.74 / (Re**0.9)
        denom_f = math.log(term1_f + term2_f, 10)**2
        f = 0.25 / denom_f
        return f
    else:
        warnings.warn("Other friction factor requires iterative models")

def classify_regime(Re):
    if Re < 2100:
        return "Laminar"
    elif 2100 <= Re <= 4000:
        return "Transitional"
    else:
        return "Turbulent"

def calc_head_loss(f, L, D, v, g=9.81):
    h_f = f*(L/D)*(v**2/2*g)
    return h_f

def calc_pressure_drop(rho, h_f, g=9.81):
    delta_p_kpa = (rho * g * h_f)/1000
    return delta_p_kpa

# variable mostly for LAMINAR
rho = 998.2
mew = 0.001002
D = 0.05
v = 1.5
f = 0.0227
L = 100
#extra variable for TURBULENT
epsilon = 0.000045

Re = calc_reynolds(rho, v, D, mew)
print(Re)
regime = classify_regime(Re)
print(regime)
darcy_friction = calc_darcy_friction(Re, epsilon, D, regime)
print(darcy_friction)
h_f= calc_head_loss(f, L, D, v)
pressure_drop = calc_pressure_drop(rho, h_f)
print(f"h_f : {h_f}\npressure drop : {pressure_drop}")