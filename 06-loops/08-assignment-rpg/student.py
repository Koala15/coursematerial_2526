def rpg2(n_sides, goal):
    trows = 0
    hits = 0
    for i in range(1, n_sides + 1):
        for j in range(1, n_sides + 1):
            sum = i + j
            trows += 1
            if sum >= goal:
                hits +=1
    return hits/trows * 100

def rpg3(n_sides, goal):
    trows = 0
    hits = 0
    for i in range(1, n_sides + 1):
        for j in range(1, n_sides + 1):
            for k in range(1, n_sides + 1):
                sum = i + j + k
                trows += 1
                if sum >= goal:
                    hits +=1
    return hits/trows * 100