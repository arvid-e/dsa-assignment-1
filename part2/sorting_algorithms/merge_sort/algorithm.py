def merge_sort(lst):
    if (len(lst) <= 1):
        return lst

    firstHalf = lst[0: len(lst) // 2]
    secondHalf = lst[len(lst) // 2: len(lst)]

    sortedFirstHalf = merge_sort(firstHalf)
    sortedSecondHalf = merge_sort(secondHalf)

    result = []
    firstP = 0
    secondP = 0

    while (firstP < len(sortedFirstHalf) and secondP < len(sortedSecondHalf)):
        if (sortedFirstHalf[firstP] < sortedSecondHalf[secondP]):
            result.append(sortedFirstHalf[firstP])
            firstP += 1
        else:
            result.append(sortedSecondHalf[secondP])
            secondP += 1

    if (firstP < len(sortedFirstHalf)):
        result.extend(sortedFirstHalf[firstP: len(sortedFirstHalf)])

    if (secondP < len(sortedSecondHalf)):
        result.extend(sortedSecondHalf[secondP: len(sortedSecondHalf)])

    return result
