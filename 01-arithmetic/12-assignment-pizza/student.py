from math import ceil
def pizza(n_people, slices_per_pizza):
    amount_pizza = ceil(n_people / slices_per_pizza)
    return amount_pizza