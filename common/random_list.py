import random


def create_random_list(n):
    list = []
    for i in range(n):
        list.append(random.randint(-10 * n, 10 * n))

    return list