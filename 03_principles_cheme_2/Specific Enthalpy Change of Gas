import sympy as sp
from sympy import integrate
import pandas as pd

gas_data = {
    "CO2": {"A": 36.11, "B": 4.233*10**-2, "C": -2.887*10**-5, "D": 7.464*10**5},
    "N2": {"A": 28.90, "B": 0.1571*10**-2, "C": 0.8081*10**-5, "D": -2.873*10**-9},
    "O2": {"A": 31.32234, "B": -20.23531, "C": 57.86644, "D": -36.50624},
    "CH4": {"A": -0.703029, "B": 108.4773, "C": -42.52157, "D": 5.862788}
}

#......................................................................

def calc_cp(T, coeff):
    cp = coeff["A"] + coeff["B"]*T + coeff["C"]*T**2 + coeff["D"]*T**-2
    return cp

def calc_delta_h(T1_degC, T2_degC, cp):
    T1_degK = T1_degC + 273.15
    T2_degK = T2_degC + 273.15
    delta_h = integrate(cp, (T, T1_degK, T2_degK))/1000
    return delta_h

#......................................................................

T = sp.Symbol("T")
gas_name = "CO2"
T1_degC = 25
T2_degC = 300

if gas_name in gas_data:
    coeff = {
        "A": gas_data[gas_name]["A"],
        "B": gas_data[gas_name]["B"],
        "C": gas_data[gas_name]["C"],
        "D": gas_data[gas_name]["D"],
    }
    cp = calc_cp(T, coeff)
    delta_h = calc_delta_h(T1_degC, T2_degC, cp)
    data = {
        "Heat Capacity":[cp],
        "Specific Enthalpy Change":[delta_h]
    }
    df = pd.DataFrame(data)
    print(df.to_string(index=False))