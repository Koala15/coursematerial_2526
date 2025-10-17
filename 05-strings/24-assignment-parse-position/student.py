def parse_position_x(string):
    s = string
    parse = s.find(',')
    open_h = s.find('(')

    if parse > -1:
        if open_h > -1:
            x = s[open_h +1 : parse]
            return float(x)
        else:
            x = s[0 : parse]
            return float(x)
    return False

def parse_position_y(string):
    s = string
    parse = s.find(',')
    end_h = s.find(')')

    if parse > -1:
        if end_h > -1:
            y = s[parse + 1: end_h]
            return float(y)
        else:
            y = s[parse + 1 : ]
            return float(y)
    return False
