def orbit_chain(orbits, start):
    chain = [start]
    while start in orbits:
        chain.append(orbits[start])
        start = orbits[start]
    return chain