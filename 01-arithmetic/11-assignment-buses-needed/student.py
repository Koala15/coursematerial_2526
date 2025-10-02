from math import ceil
def buses_needed(people_count, bus_capacity):
    amount_buses = people_count / bus_capacity
    return ceil(amount_buses)