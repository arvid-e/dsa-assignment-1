from common.measure import average, measure
from common.plots import (
    PART2_FIGURES_DIR,
    plot_average_comparison,
    plot_loglog_comparison,
    use_figures_dir,
)
from common.random_list import create_random_positive_list
from part2.sorting_algorithms.bucket_sort.algorithm import bucket_sort
from part2.sorting_algorithms.radix_sort.algorithm import radix_sort_lsd

SIZES = [10000, 20000, 40000, 80000, 160000, 320000, 640000]

RUNS = 5

ALGORITHMS = {
    'Bucket sort': bucket_sort,
    'Radix sort': radix_sort_lsd,
}


def run():
    use_figures_dir(PART2_FIGURES_DIR)

    averages_by_name = {}

    for name, algorithm in ALGORITHMS.items():
        print(f"--- {name} ---")
        # Bucket sort and radix sort only handle non negative numbers
        averages_by_name[name] = average(
            measure(algorithm, SIZES, runs=RUNS,
                    create=create_random_positive_list))

    plot_average_comparison(SIZES, averages_by_name,
                            f'Figure 5: Average of {RUNS} runs: ' +
                            'bucket sort vs radix sort',
                            'figure5_bucket_radix_comparison.png')

    ks = plot_loglog_comparison(SIZES, averages_by_name,
                                'Figure 5a: Log-log plot with linear fit: ' +
                                'bucket sort vs radix sort',
                                'figure5a_bucket_radix_comparison.png')

    for name, k in ks.items():
        print(f"{name}: estimated exponent k = {k:.3f}")


if __name__ == '__main__':
    run()
