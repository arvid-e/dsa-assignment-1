import random


def create_random_list(n):
    list = []
    for i in range(n):
        list.append(random.randint(-10 * n, 10 * n))

    return list


# Radix sort does one pass per digit, so a value range that grows with n
# would add a pass every time n reaches a new power of 10. Keeping the
# range fixed keeps the number of digits constant.
MAX_VALUE = 999999


def create_random_positive_list(n, max_value=MAX_VALUE):
    list = []
    for i in range(n):
        list.append(random.randint(0, max_value))

    return list
