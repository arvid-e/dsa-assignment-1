def threesum_pointers(lst, sum=0):
    res = set()
    lst.sort()

    for i in range(len(lst) - 2):
        left = i + 1
        right = len(lst) - 1

        while (left < right):
            currentSum = lst[i] + lst[left] + lst[right]

            if (currentSum > sum):
                right -= 1
            elif (currentSum < sum):
                left += 1
            else:
                res.add(tuple(sorted([lst[i], lst[left], lst[right]])))
                right -= 1
                left += 1

    return res
