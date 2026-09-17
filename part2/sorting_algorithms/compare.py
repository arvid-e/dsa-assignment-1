from common.measure import SIZES, average, measure
from common.plots import plot_average_comparison, plot_loglog_comparison
from part2.sorting_algorithms.bubble_sort.algorithm import bubble_sort
from part2.sorting_algorithms.insertion_sort.algorithm import insertion_sort
from part2.sorting_algorithms.selection_sort.algorithm import selection_sort

ALGORITHMS = {
    'Bubble sort': bubble_sort,
    'Insertion sort': insertion_sort,
    'Selection sort': selection_sort,
}


def run():
    averages_by_name = {}

    for name, algorithm in ALGORITHMS.items():
        print(f"--- {name} ---")
        averages_by_name[name] = average(measure(algorithm, SIZES))

    plot_average_comparison(SIZES, averages_by_name,
                            'Average of 3 runs per sorting algorithm',
                            'sorting_comparison_averages.png')

    ks = plot_loglog_comparison(SIZES, averages_by_name,
                                'Log-log plot with linear fit ' +
                                'per sorting algorithm',
                                'sorting_comparison_loglog.png')

    for name, k in ks.items():
        print(f"{name}: estimated exponent k = {k:.3f}")


if __name__ == '__main__':
    run()
