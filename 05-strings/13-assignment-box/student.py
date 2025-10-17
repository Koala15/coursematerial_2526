def box(string):
    length = len(string)
    side = '+-' + (length * '-') + '-+'
    return f"{side}\n| {string} |\n{side}"
