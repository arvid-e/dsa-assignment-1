from common.measure import average, measure
from common.plots import plot_average_comparison, plot_loglog_comparison
from part2.sorting_algorithms.merge_sort.algorithm import merge_sort
from part2.sorting_algorithms.quick_sort.algorithm import quick_sort

# Use large sizes for Merge sort and Quick sort since they are much faster
SIZES = [60000, 70000, 80000, 90000, 100000, 110000, 120000]

ALGORITHMS = {
    'Merge sort': merge_sort,
    'Quick sort': quick_sort,
}


def run():
    averages_by_name = {}

    for name, algorithm in ALGORITHMS.items():
        print(f"--- {name} ---")
        averages_by_name[name] = average(measure(algorithm, SIZES))

    plot_average_comparison(SIZES, averages_by_name,
                            'Average of 3 runs: merge sort vs quick sort',
                            'merge_quick_comparison_averages.png')

    ks = plot_loglog_comparison(SIZES, averages_by_name,
                                'Log-log plot with linear fit: ' +
                                'merge sort vs quick sort',
                                'merge_quick_comparison_loglog.png')

    for name, k in ks.items():
        print(f"{name}: estimated exponent k = {k:.3f}")


if __name__ == '__main__':
    run()
