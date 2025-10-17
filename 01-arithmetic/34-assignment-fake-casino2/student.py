import random

def generate_number(n):
    return round(random.uniform(1,n), 1)
# num = 1 + (n - 1) * random.random()
# return round(num, 1)
    
def fake_casino_revisited(n):
    random.seed(42)
    print(generate_number(n))
    print(generate_number(n))
    print(generate_number(n))
    print(generate_number(n))
    print(generate_number(n))