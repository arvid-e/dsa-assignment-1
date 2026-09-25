import math

from common.linear_regression import lin_reg
from common.measure import SIZES, average, measure
from common.plots import (
    PART2_FIGURES_DIR,
    plot_average_comparison,
    plot_loglog_comparison,
    plot_ratio,
    use_figures_dir,
)
from part2.sorting_algorithms.bubble_sort.algorithm import bubble_sort
from part2.sorting_algorithms.insertion_sort.algorithm import insertion_sort
from part2.sorting_algorithms.selection_sort.algorithm import selection_sort

ALGORITHMS = {
    'Bubble sort': bubble_sort,
    'Insertion sort': insertion_sort,
    'Selection sort': selection_sort,
}


def print_constants(sizes, averages_by_name):
    # From log(T) = m + k*log(n) we get T(n) = c * n^k with c = e^m
    log_sizes = [math.log(n) for n in sizes]
    cs = {}

    for name, averages in averages_by_name.items():
        log_times = [math.log(t) for t in averages]
        m, k = lin_reg(log_sizes, log_times)
        cs[name] = math.exp(m)
        print(f"{name}: m = {m:.3f}, k = {k:.3f}, c = e^m = {cs[name]:.3e}")

    bubble = cs['Bubble sort']
    insertion = cs['Insertion sort']
    print(f"c(Bubble) / c(Insertion) = {bubble:.3e} / {insertion:.3e} "
          f"= {bubble / insertion:.2f}")


def print_time_ratios(sizes, averages_by_name):
    # Simpler check: divide the measured times at the same input size
    print(f"{'n':>6} | {'T_Bubble (s)':>12} | {'T_Insertion (s)':>15} | ratio")

    for i, n in enumerate(sizes):
        bubble = averages_by_name['Bubble sort'][i]
        insertion = averages_by_name['Insertion sort'][i]
        print(f"{n:>6} | {bubble:>12.4f} | {insertion:>15.4f} | "
              f"{bubble / insertion:.2f}")


def run():
    use_figures_dir(PART2_FIGURES_DIR)

    averages_by_name = {}

    for name, algorithm in ALGORITHMS.items():
        print(f"--- {name} ---")
        averages_by_name[name] = average(measure(algorithm, SIZES))

    plot_average_comparison(SIZES, averages_by_name,
                            'Figure 3: Average of 3 runs ' +
                            'per sorting algorithm',
                            'figure3_sorting_comparison.png')

    ks = plot_loglog_comparison(SIZES, averages_by_name,
                                'Figure 3a: Log-log plot with linear fit ' +
                                'per sorting algorithm',
                                'figure3a_sorting_comparison.png')

    for name, k in ks.items():
        print(f"{name}: estimated exponent k = {k:.3f}")

    print_constants(SIZES, averages_by_name)
    print_time_ratios(SIZES, averages_by_name)

    plot_ratio(SIZES, averages_by_name['Bubble sort'],
               averages_by_name['Insertion sort'],
               'T_Bubble(n) / T_Insertion(n)',
               'Figure 8: Bubble sort time relative to insertion sort',
               'figure8_bubble_insertion_ratio.png')


if __name__ == '__main__':
    run()
