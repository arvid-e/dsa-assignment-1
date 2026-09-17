
from common.measure import measure, average, SIZES
from common.plots import (
    plot_runs,
    plot_average,
    plot_loglog_fit,
)
from part2.sorting_algorithms.insertion_sort.algorithm import insertion_sort


def run():
    all_runs = measure(insertion_sort, SIZES)
    averages = average(all_runs)

    plot_runs(SIZES, all_runs,
              'Figure 2: 3 separate runs', 'insertion_sort.png')
    plot_average(SIZES, averages,
                 'Figure 2a: Average of 3 runs', 'insertion_sort_averages.png')
    k = plot_loglog_fit(SIZES, averages,
                        'Insertion sort: Log-log plot with linear fit',
                        'insertion_sort_loglog.png')

    print(f"Estimated time complexity exponent (k): {k:.3f}")


if __name__ == '__main__':
    run()
