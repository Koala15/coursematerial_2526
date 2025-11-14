def remove_duplicates(xs):
    new_list = []
    copy_set = set()
    for i in xs:
        if len(new_list) == 0:
            new_list.append(i)
            copy_set.add(i)
        elif not (i in copy_set):
            new_list.append(i)
            copy_set.add(i)
    return new_list