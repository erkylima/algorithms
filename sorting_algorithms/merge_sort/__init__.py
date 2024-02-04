def merge_sort(ordering):
    length = len(ordering)
    if length > 1:
        half = length // 2
        left_list = ordering[:half]  # Left List
        right_list = ordering[half:]  # Right List
        merge_sort(left_list)
        merge_sort(right_list)

        i, j, k = 0, 0, 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                ordering[k] = left_list[i]
                i += 1
            else:
                ordering[k] = right_list[j]
                j += 1
            k += 1
        while i < len(left_list):
            ordering[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            ordering[k] = right_list[j]
            j += 1
            k += 1
