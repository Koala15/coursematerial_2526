import random

def roll_dice(n):
    return random.randint(1, n)

def fake_casino(n):
    random.seed(42)
    print(roll_dice(n))
    print(roll_dice(n))
    print(roll_dice(n))
    print(roll_dice(n))
    print(roll_dice(n))