water_density_kgm3 = 999.01

def api_to_density(api_val):
    sg = 141.5 / (api_val + 131.5)
    density = sg * water_density_kgm3
    return sg, density

def classify_crude(api_val):
    if api_val >= 31.1:
        return "Light Crude"
    elif api_val >= 22.3:
        return "Medium Crude"
    elif api_val >= 10.0:
        return "Heavy Crude"
    else:
        return "Extra Heavy Crude / Bitumen"

api_val = 43.0
a= classify_crude(api_val)
b =api_to_density(api_val)
print(f"Crude Classification: {a}\nAPI to density: {b}")