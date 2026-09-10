import random


def create_random_list(n):
    list = []
    for i in range(n):
        list.append(random.randint(-10, 10))

    return list