def player_movement(position, left_arrow, right_arrow, shift):
    p = position
    la = left_arrow
    ra = right_arrow
    s = shift
    
    if la == True:
        if s == True:
            p -= 2
        else:
            p -= 1
            
    if ra == True:
        if s == True:
           p += 2
        else:
            p += 1
    
    return p