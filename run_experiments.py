import sys

from common import plots
from part1.threesum import correctness
from part1.threesum.bruteforce import main as threesum_bruteforce
from part1.threesum.two_pointers import main as threesum_two_pointers
from part2.sorting_algorithms import (
    compare,
    compare_all,
    compare_bucket_radix,
    compare_digits,
    compare_merge_quick,
)
from part2.sorting_algorithms.bubble_sort import main as bubble_sort
from part2.sorting_algorithms.insertion_sort import main as insertion_sort
from part2.sorting_algorithms.selection_sort import main as selection_sort

EXPERIMENTS = {
    'threesum_correctness': correctness,
    'threesum_bruteforce': threesum_bruteforce,
    'threesum_two_pointers': threesum_two_pointers,
    'bubble_sort': bubble_sort,
    'insertion_sort': insertion_sort,
    'selection_sort': selection_sort,
    'compare_simple_sorts': compare,
    'compare_merge_quick': compare_merge_quick,
    'compare_bucket_radix': compare_bucket_radix,
    'compare_digits': compare_digits,
    'compare_all': compare_all,
}


def run(names):
    for name in names:
        print(f"\n=== {name} ===")
        # Part 2 experiments switch the figures folder, so reset it to the
        # default each time to save figures where the file alone would
        plots.use_figures_dir(plots.ROOT / "figures")
        EXPERIMENTS[name].run()


if __name__ == '__main__':
    names = sys.argv[1:] or list(EXPERIMENTS)

    unknown = [name for name in names if name not in EXPERIMENTS]
    if unknown:
        print(f"Unknown experiment(s): {', '.join(unknown)}")
        print(f"Available: {', '.join(EXPERIMENTS)}")
        sys.exit(1)

    run(names)
