def bubble_sort(lst):
    copy = lst.copy()
    swapped = True

    while (swapped):
        swapped = False

        for i in range(len(copy) - 1):
            if (copy[i] > copy[i + 1]):
                helper = copy[i]
                copy[i] = copy[i + 1]
                copy[i + 1] = helper
                swapped = True

    return copy
