def quick_sort(ordering):
    length = len(ordering)
    if length <= 1:
        return ordering
    pivot = ordering[0]
    equal = [x for x in ordering if x == pivot]
    lesser = [x for x in ordering if x < pivot]
    greater = [x for x in ordering if x > pivot]
    return quick_sort(lesser) + equal + quick_sort(greater)
