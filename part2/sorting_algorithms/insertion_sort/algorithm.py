def insertion_sort(lst):
    for i in range(1, len(lst)):
        current = lst[i]

        right = i
        left = right - 1

        if (lst[right] > lst[left]):
            continue

        while (left >= 0):
            if (current < lst[left]):
                lst[right] = lst[left]

                if (left < 1):
                    lst[left] = current
            else:
                lst[right] = current
                break

            left -= 1
            right -= 1

    return lst


lst = [4, 1, 2, 0, 5, 3]
print(insertion_sort(lst))
