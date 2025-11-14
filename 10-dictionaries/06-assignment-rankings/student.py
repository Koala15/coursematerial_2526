def rankings(participants):
    ranking = {}
    rank = 1
    for p in participants:
        ranking[p] = rank
        rank += 1
    return ranking