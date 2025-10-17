def tip_calculator():
    price = input("Enter total price: ")
    tip = input("Enter tip percentage (default=20): ")

    if tip == "":
        tip = 20
    else:
        tip = int(tip)

    pay = int(price) * ((tip / 100) + 1)
    pay = round(pay)
    print(f"You have to pay {pay}")