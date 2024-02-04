def selection_sort(ordering):
    length = len(ordering)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if ordering[j] < ordering[min_index]:
                min_index = j

        ordering[min_index], ordering[i] = ordering[i], ordering[min_index]

