import numpy as np

def calc_vdw_compressibility(P, T, a, b, R=0.08206):
    c2 = -(b+ (R*T/P))
    c1 = a/P
    c0 = -a*b/P
    roots = np.roots([1.0, c2, c1, c0])
    real_roots = roots[np.abs(roots.imag) < 10**-6].real
    if real_roots.size == 1:
        V_molar = real_roots
        Z = (P*V_molar) / (R*T)
        return Z, V_molar
    elif real_roots.size == 3:
        V_liq = min(real_roots)
        V_vap = max(real_roots)
        Z_liq = (P*V_liq) / (R*T)
        Z_vap = (P*V_vap) / (R*T)
        return Z_liq, V_liq, Z_vap, V_vap

P = 10
T = 250
a = 3.59
b = 0.0427
result = calc_vdw_compressibility(P, T, a, b)
print(result)