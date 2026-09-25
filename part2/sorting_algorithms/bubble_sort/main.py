from common.measure import measure, average, SIZES
from common.plots import (
    PART2_FIGURES_DIR,
    use_figures_dir,
    plot_runs,
    plot_average,
    plot_loglog_fit,
)

from part2.sorting_algorithms.bubble_sort.algorithm import bubble_sort


def run():
    use_figures_dir(PART2_FIGURES_DIR)

    all_runs = measure(bubble_sort, SIZES)
    averages = average(all_runs)

    plot_runs(SIZES, all_runs,
              'Figure 3: 3 separate runs', 'figure3_bubble_sort.png')
    plot_average(SIZES, averages,
                 'Figure 3a: Average of 3 runs',
                 'figure3a_bubble_sort.png')
    k = plot_loglog_fit(SIZES, averages,
                        'Figure 3b: Log-log plot with linear fit',
                        'figure3b_bubble_sort.png')

    print(f"Estimated time complexity exponent (k): {k:.3f}")


if __name__ == '__main__':
    run()