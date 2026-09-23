def threesum_brute(lst, sum=0):
    sums = set()

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                if (lst[i] + lst[j] + lst[k] == sum):
                    sums.add(tuple(sorted([lst[i], lst[j], lst[k]])))

    res = []
    for t in sums:
        res.append(t)

    return res
