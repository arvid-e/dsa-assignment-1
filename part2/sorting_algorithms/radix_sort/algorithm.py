def radix_sort_lsd(lst):
    largest = lst[0]
    for i in range(len(lst)):
        largest = max(largest, lst[i])

    longestDigit = len(str(largest))
    currentLst = lst[:]

    for i in range(longestDigit):
        buckets = [[] for _ in range(10)]

        for j in range(len(currentLst)):
            digit = (currentLst[j] // 10**i) % 10
            buckets[digit].append(currentLst[j])

        currentLst = []
        for j in range(len(buckets)):
            currentLst.extend(buckets[j])

    return currentLst
