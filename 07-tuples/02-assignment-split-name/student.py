def split_name(full_name):
    space = full_name.find(' ')
    split_name = (full_name[:space], full_name[space + 1:])
    return split_name