def selection_sort(lst):
    copy = lst.copy()

    for left in range(len(copy)):

        smallest = copy[left]
        smallestIndex = left
        for right in range(left, len(copy)):
            if (copy[right] < smallest):
                smallest = copy[right]
                smallestIndex = right

        if (smallest == copy[left]):
            continue

        helper = copy[left]
        copy[left] = smallest
        copy[smallestIndex] = helper

    return copy


copy = [2, 1, 4, 3]
print(selection_sort(copy))

print(copy)
