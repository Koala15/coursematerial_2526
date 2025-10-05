from math import ceil
def internet_costs(duration_in_seconds, cost_per_block):
    blocks = ceil(duration_in_seconds / 360)
    cost = blocks * cost_per_block
    return cost