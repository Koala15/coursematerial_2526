def is_digit(char):
    if ('0' <= char[0] <= '9') and ('0' <= char[1] <= '9') and ('0' <= char[2] <= '9') and ('0' <= char[3] <= '9') and ('0' <= char[4] <= '9') and ('0' <= char[5] <= '9') and ('0' <= char[6] <= '9'):
        return True
    return False


def is_student_id(string):
    str_len = len(string)
    f_char = string[0]
    rest = string[1:]

    if str_len == 8:
        if (f_char == 'R') or (f_char == 'S') or (f_char == 'r') or (f_char == 's'):
            if is_digit(rest) == True:
                return True
    return False