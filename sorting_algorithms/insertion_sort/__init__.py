
class InsertionSort:
    def __init__(self, ordering):
        length = len(ordering)
        for i in range(1, length):
            k = i
            while k > 0 and ordering[k] < ordering[k-1]:
                ordering[k], ordering[k-1] = ordering[k-1], ordering[k]
                k -= 1
        print(ordering)

