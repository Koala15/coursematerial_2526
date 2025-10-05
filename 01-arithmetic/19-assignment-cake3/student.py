def cake3(eggs, flour, butter, sugar):
    amount_e = eggs // 5
    amount_f = flour // 250
    amount_b = butter // 200
    amount_s = sugar // 250

    return min(amount_e, amount_f, amount_b, amount_s)