def desktop(catalog, components):
    sum = 0
    for comp in components:
        sum += catalog[comp]
    return sum