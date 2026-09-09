def calc_dof(nu, ns, nspec, nsum):
    eqn_total = ns + nspec + nsum
    dof = nu - eqn_total

    if dof == 0:
        stat = "Exactly Specified (Solvable)"
    elif dof > 0:
        stat = "Under-specified (Need more equations / constraints)"
    else:
        stat = "Over-specified (Too many constraints)"

    return dof, stat

nu = 4
ns = 2
nspec = 1
nsum = 1
dof, status = calc_dof(nu, ns, nspec, nsum)
print(f"DoF: {dof}\nStatus: {status}")