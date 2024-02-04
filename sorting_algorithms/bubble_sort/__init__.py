
def bubble_sort(ordering):
    length = len(ordering)
    for i in range(length-1, 0, -1):
        for j in range(i):
            if ordering[j] > ordering[j+1]:
                ordering[j], ordering[j+1] = ordering[j+1], ordering[j]

