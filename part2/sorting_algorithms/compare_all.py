from common.measure import average, measure
from common.plots import (
    PART2_FIGURES_DIR,
    plot_average_comparison,
    plot_loglog_comparison,
    use_figures_dir,
)
from common.random_list import create_random_positive_list
from part2.sorting_algorithms.bucket_sort.algorithm import bucket_sort
from part2.sorting_algorithms.merge_sort.algorithm import merge_sort
from part2.sorting_algorithms.quick_sort.algorithm import quick_sort
from part2.sorting_algorithms.radix_sort.algorithm import radix_sort_lsd

SIZES = [10000, 20000, 40000, 80000, 160000, 320000, 640000]

RUNS = 5

ALGORITHMS = {
    'Bucket sort': bucket_sort,
    'Radix sort': radix_sort_lsd,
    'Merge sort': merge_sort,
    'Quick sort': quick_sort,
}


def run():
    use_figures_dir(PART2_FIGURES_DIR)

    averages_by_name = {}

    for name, algorithm in ALGORITHMS.items():
        print(f"--- {name} ---")
        # All four run on the same kind of input (non negative numbers)
        # since bucket sort and radix sort cannot handle negative numbers
        averages_by_name[name] = average(
            measure(algorithm, SIZES, runs=RUNS,
                    create=create_random_positive_list))

    plot_average_comparison(SIZES, averages_by_name,
                            f'Figure 7: Average of {RUNS} runs: ' +
                            'bucket, radix, ' +
                            'merge and quick sort',
                            'figure7_all_sorts_comparison.png')

    ks = plot_loglog_comparison(SIZES, averages_by_name,
                                'Figure 7a: Log-log plot with linear fit: ' +
                                'bucket, radix, ' +
                                'merge and quick sort',
                                'figure7a_all_sorts_comparison.png')

    for name, k in ks.items():
        print(f"{name}: estimated exponent k = {k:.3f}")


if __name__ == '__main__':
    run()
