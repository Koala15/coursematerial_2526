from math import ceil
def movie_ticket(duration, imax, student, ticket_count):
    d = duration
    price = 0

    if d < 90:
        price += 10
    elif 90 < d < 120:
        price += 11
    elif 120 < d < 150:
        price += 12
    elif 150 < d:
        price += 15
    
    if imax:
        price *= 1.2
        ceil(price)
    
    if student:
        price -= 3
    
    return price * ticket_count