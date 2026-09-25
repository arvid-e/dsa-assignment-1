import time

from common.measure import average
from common.plots import (
    PART2_FIGURES_DIR,
    plot_comparison,
    use_figures_dir,
)
from common.random_list import create_random_positive_list
from part2.sorting_algorithms.bucket_sort.algorithm import bucket_sort
from part2.sorting_algorithms.radix_sort.algorithm import radix_sort_lsd

# Input size is fixed here, it is the value range that varies. Radix sort
# does one pass per digit, so its running time should grow with the number
# of digits while bucket sort should stay flat
SIZE = 200000

DIGITS = [3, 4, 5, 6, 7, 8, 9]

RUNS = 5

ALGORITHMS = {
    'Bucket sort': bucket_sort,
    'Radix sort': radix_sort_lsd,
}


def measure_digits(algorithm, digits, runs=RUNS):
    all_runs = []

    for run in range(runs):
        measurements = []

        for d in digits:
            max_value = 10 ** d - 1
            lst = create_random_positive_list(SIZE, max_value)
            start = time.perf_counter()
            algorithm(lst)
            end = time.perf_counter()
            elapsed = end - start
            measurements.append(elapsed)
            print(f"run {run + 1}: digits={d}, time={elapsed:.4f}s")

        all_runs.append(measurements)

    return all_runs


def run():
    use_figures_dir(PART2_FIGURES_DIR)

    averages_by_name = {}

    for name, algorithm in ALGORITHMS.items():
        print(f"--- {name} ---")
        averages_by_name[name] = average(measure_digits(algorithm, DIGITS))

    plot_comparison(DIGITS, averages_by_name,
                    'Number of digits in the values',
                    f'Figure 6: Average of {RUNS} runs at n = {SIZE}: '
                    'effect of the value range',
                    'figure6_bucket_radix_digits.png')

    for name, averages in averages_by_name.items():
        times = ', '.join(f"{t:.3f}s" for t in averages)
        print(f"{name}: {times}")


if __name__ == '__main__':
    run()
