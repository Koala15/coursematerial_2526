def sum_input():
    sum = 0
    while 1:
        i = int(input("Enter integer: "))
        if i == 0:
            break
        sum += i
    
    print(f"The sum equals {sum}.")
        