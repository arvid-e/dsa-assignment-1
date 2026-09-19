from part2.sorting_algorithms.insertion_sort.algorithm import insertion_sort
import math


def bucket_sort(lst):
    largest = lst[0]
    for i in range(len(lst)):
        largest = max(largest, lst[i])

    buckets = [[] for _ in range(len(lst))]

    for i in range(len(lst)):
        normalized = lst[i] / (largest + 1)
        bucket = math.floor(len(lst) * normalized)
        buckets[bucket].append(lst[i])

    res = []
    for i in range(len(buckets)):
        if (buckets[i] == []):
            continue

        insertion_sort(buckets[i])
        res.extend(buckets[i])
    return res
