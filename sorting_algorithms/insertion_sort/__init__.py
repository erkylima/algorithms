
def insertion_sort(ordering):
    length = len(ordering)
    for i in range(1, length):
        k = i
        while k > 0 and ordering[k] < ordering[k-1]:
            ordering[k], ordering[k-1] = ordering[k-1], ordering[k]
            k -= 1


