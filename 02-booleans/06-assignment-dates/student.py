def is_valid_month(month):
    if 1 <= month <= 12:
        return True
    return False

def is_leap_year(year):
    if year % 4 == False:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def has_30_days(month):
    m = month
    if m == 4 or m == 6 or m == 9 or m == 11:
        return True
    return False

def has_31_days(month):
    m = month
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return True
    return False

def has_28_days(month, year):
    m = month
    y = is_leap_year(year)
    if y != True and m == 2:
        return True
    return False

def has_29_days(month, year):
    m = month
    y = is_leap_year(year)
    if y and m == 2:
        return True
    return False

def is_valid_date(day, month, year):
    d = day
    m = month
    y = year

    d_28 = has_28_days(m, y)
    d_29 = has_29_days(m, y)
    d_30 = has_30_days(m)
    d_31 = has_31_days(m)
    
    if is_valid_month(m) == True:
        if (d_31 == True and 1 <= d <= 31) or (d_30 == True and 1 <= d <= 30) or (d_29 == True and 1 <= d <= 29) or (d_28 == True and 1 <= d <= 28):
            return True
    return False