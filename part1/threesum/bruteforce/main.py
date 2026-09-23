from part1.threesum.bruteforce.algorithm import threesum_brute
from common.measure import measure, average
from common.plots import (
    plot_runs,
    plot_average,
    plot_loglog_fit,
)


SIZES = list(range(210, 701, 35))


def run():
    all_runs = measure(threesum_brute, SIZES)
    averages = average(all_runs)

    plot_runs(SIZES, all_runs,
              'Figure 1: 3 separate runs', 'figure1_brute_force.png')
    plot_average(SIZES, averages,
                 'Figure 1a: Average of 3 runs', 'figure1a_brute_force.png')
    k = plot_loglog_fit(SIZES, averages,
                        'Figure 1b: Log-log plot with linear fit',
                        'figure1b_brute_force.png')

    print(f"Estimated time complexity exponent (k): {k:.3f}")


if __name__ == '__main__':
    run()
