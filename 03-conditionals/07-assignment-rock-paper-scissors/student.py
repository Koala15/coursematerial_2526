def rock_paper_scissors(p1_choice, p2_choice):
    p1 = p1_choice
    p2 = p2_choice
    if p1 == p2:
        return 0
    elif p1 > p2:
        if p2 == 0 and p1 == 2:
            return 2
        return 1
    elif p1 < p2:
        if p1 == 0 and p2 == 2:
            return 1
        return 2