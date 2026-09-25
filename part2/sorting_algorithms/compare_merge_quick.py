from common.measure import average, measure
from common.plots import (
    PART2_FIGURES_DIR,
    plot_average_comparison,
    plot_loglog_comparison,
    use_figures_dir,
)
from part2.sorting_algorithms.merge_sort.algorithm import merge_sort
from part2.sorting_algorithms.quick_sort.algorithm import quick_sort

# Use large sizes for Merge sort and Quick sort since they are much faster
SIZES = [60000, 70000, 80000, 90000, 100000, 110000, 120000]

ALGORITHMS = {
    'Merge sort': merge_sort,
    'Quick sort': quick_sort,
}


def run():
    use_figures_dir(PART2_FIGURES_DIR)

    averages_by_name = {}

    for name, algorithm in ALGORITHMS.items():
        print(f"--- {name} ---")
        averages_by_name[name] = average(measure(algorithm, SIZES))

    plot_average_comparison(SIZES, averages_by_name,
                            'Figure 4: Average of 3 runs: ' +
                            'merge sort vs quick sort',
                            'figure4_merge_quick_comparison.png')

    ks = plot_loglog_comparison(SIZES, averages_by_name,
                                'Figure 4a: Log-log plot with linear fit: ' +
                                'merge sort vs quick sort',
                                'figure4a_merge_quick_comparison.png')

    for name, k in ks.items():
        print(f"{name}: estimated exponent k = {k:.3f}")


if __name__ == '__main__':
    run()
