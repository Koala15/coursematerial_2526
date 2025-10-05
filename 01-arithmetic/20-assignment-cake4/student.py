def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    amount_e = eggs // eggs_per_cake
    amount_f = flour // flour_per_cake
    amount_b = butter // butter_per_cake
    amount_s = sugar // sugar_per_cake
    return min(amount_e, amount_f, amount_b, amount_s)