from part1.threesum.two_pointers.algorithm import threesum_pointers
from common.measure import measure, average
from common.plots import (
    plot_runs,
    plot_average,
    plot_loglog_fit,
)


SIZES = [500, 1000, 2000, 3000, 4000, 5000]


def run():
    all_runs = measure(threesum_pointers, SIZES)
    averages = average(all_runs)

    plot_runs(SIZES, all_runs,
              'Figure 2: 3 separate runs', 'figure2_two_pointers.png')
    plot_average(SIZES, averages,
                 'Figure 2a: Average of 3 runs', 'figure2a_two_pointers.png')
    k = plot_loglog_fit(SIZES, averages,
                        'Figure 2b: Log-log plot with linear fit',
                        'figure2b_two_pointers.png')

    print(f"Estimated time complexity exponent (k): {k:.3f}")


if __name__ == '__main__':
    run()
