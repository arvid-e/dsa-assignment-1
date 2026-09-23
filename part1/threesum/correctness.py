from common.random_list import create_random_list
from part1.threesum.bruteforce.algorithm import threesum_brute
from part1.threesum.two_pointers.algorithm import threesum_pointers

SIZE = 15

LISTS = 3


def run():
    for i in range(LISTS):
        lst = create_random_list(SIZE)

        brute = sorted(threesum_brute(lst))
        pointers = sorted(threesum_pointers(lst))

        print(f"--- list {i + 1} ---")
        print(f"Input:  {lst}")
        print(f"Result: {brute}")

        if brute == pointers:
            print("Both implementations agree")
        else:
            print(f"MISMATCH, two pointers gave: {pointers}")


if __name__ == '__main__':
    run()
