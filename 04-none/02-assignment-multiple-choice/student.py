def multiple_choice(right_answer, given_answer):
    ra = right_answer
    ga = given_answer
    
    if ga is None:
        return 0
    elif ga == ra:
        return 1
    elif ga != ra:
        return -0.2