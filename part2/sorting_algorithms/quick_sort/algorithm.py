def quick_sort(lst):
    lst = lst[:]
    if (len(lst) < 2):
        return lst

    pivot = len(lst) - 1
    left = -1

    for right in range(pivot):
        if (lst[right] < lst[pivot]):
            left += 1
            helper = lst[left]
            lst[left] = lst[right]
            lst[right] = helper

    helper = lst[left + 1]
    lst[left + 1] = lst[pivot]
    lst[pivot] = helper

    sortedFirstHalf = quick_sort(lst[0: left + 1])
    sortedSecondHalf = quick_sort(lst[left + 2: len(lst)])

    return sortedFirstHalf + [lst[left + 1]] + sortedSecondHalf
