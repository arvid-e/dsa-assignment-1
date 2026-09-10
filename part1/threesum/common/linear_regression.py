def lin_reg(x, y):
    xMean = sum(x) / len(x)
    yMean = sum(y) / len(y)

    numenator = 0
    xDeviations = []

    for i in range(len(x)):
        xDeviation = x[i] - xMean
        yDeviation = y[i] - yMean 
        numenator += (xDeviation * yDeviation)
        xDeviations.append(xDeviation)

    denominator = 0

    for dev in xDeviations:
        denominator += dev * dev

    k = numenator / denominator
    m = yMean - k * xMean

    return m, k
