def is_capitalized(string):
    s = string
    if s != '':
        if s[0] == s[0].upper() and s[1:] == s[1:].lower():
            return True
    return False