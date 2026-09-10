import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import linregress

def determine_order(t_arr, c_arr):
    y_0th = c_arr
    y_1st = np.log(c_arr)
    y_2nd = 1 / c_arr
    m0, y_int0, r0, _, _ = linregress(t_arr, y_0th)
    m1, y_int1, r1, _, _ = linregress(t_arr, y_1st)
    m2, y_int2, r2, _, _ = linregress(t_arr, y_2nd)
    r_squared_0th = r0**2
    r_squared_1st = r1**2
    r_squared_2nd = r2**2
    r_squared = [
        {"Order":"0th Order", "r_squared": r_squared_0th},
        {"Order":"1st Order", "r_squared": r_squared_1st},
        {"Order":"2nd Order", "r_squared": r_squared_2nd}
    ]
    highest_r_squared = max(r_squared, key=lambda x: x["r_squared"])
    best_order = highest_r_squared["Order"]
    print(f"Best Order: {best_order}")
    if best_order == "0th Order":
        k = -m0
    elif best_order == "1st Order":
        k = -m1
    elif best_order == "2nd Order":
        k = m2
    return best_order, k
    
t_exp = np.array([0, 10, 20, 30, 40, 50, 60])
c_exp = np.array([2.00, 1.21, 0.74, 0.45, 0.27, 0.16, 0.10])
print(determine_order(t_exp, c_exp))