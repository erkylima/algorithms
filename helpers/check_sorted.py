def check_sorted(list):
    flag = False
    i = 1
    while i < len(list):
        if (list[i] > list[i - 1]):
            flag = True
        i += 1
    return flag