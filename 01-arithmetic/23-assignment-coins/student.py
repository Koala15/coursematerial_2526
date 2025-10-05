#from math import floor
def coins(amount):
    coin_5 = amount // 5
    amount %= 5
    coin_2 = amount // 2
    amount %= 2
    sum = amount + coin_2 + coin_5
    return sum