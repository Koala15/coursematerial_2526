def entrance_exam(g1, g2, g3, g4, g5):
    skip = 0
    taken = 5
    total_g = 0

    if g1 is None:
        skip += 1
        taken -= 1
        g1 = 0

    if g2 is None:
        skip += 1
        taken -= 1
        g2 = 0

    if g3 is None:
        skip += 1
        taken -= 1
        g3 = 0

    if g4 is None:
        skip += 1
        taken -= 1
        g4 = 0

    if g5 is None:
        skip += 1
        taken -= 1
        g5 = 0
    
    if skip < 2:
        total_g = (g1 + g2 + g3 + g4 + g5) / taken
        
    if total_g >= 12 and skip < 2:
        return True
    return False