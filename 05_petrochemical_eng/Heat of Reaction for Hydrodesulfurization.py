standard_hf = {
    'C4H4S': 115.1,
    'H2': 0.0,
    'C4H10': -126.15,
    'H2S': -20.6
}

def calc_hds_heat(thiophene_mol):
    nu_thiophene = -1
    nu_h2 = -4
    nu_butane = 1
    nu_h2s = 1

    h2_mol_needed = thiophene_mol* abs(nu_h2)
    delta_H_rxn = (nu_butane * standard_hf['C4H10'] + nu_h2s * standard_hf['H2S']) + (nu_thiophene * standard_hf['C4H4S'] + nu_h2 * standard_hf['H2'])
    heat_total = delta_H_rxn * thiophene_mol
    return h2_mol_needed, heat_total

required_h2, total_heat = calc_hds_heat(100)
print(f"H2 moles required: {required_h2}\nTotal Heat absorbed/released: {total_heat*1000}")