import time

from common.random_list import create_random_list


SIZES = [1000, 2000, 3000, 4000, 5000, 6000, 7000]


def measure(algorithm, sizes, runs=3, create=create_random_list):
    all_runs = []

    for run in range(runs):
        measurements = []

        for size in sizes:
            lst = create(size)
            start = time.perf_counter()
            algorithm(lst)
            end = time.perf_counter()
            elapsed = end - start
            measurements.append(elapsed)
            print(f"run {run + 1}: n={size}, time={elapsed:.4f}s")

        all_runs.append(measurements)

    return all_runs


def average(all_runs):
    averages = []

    for i in range(len(all_runs[0])):
        total = sum(run[i] for run in all_runs)
        averages.append(total / len(all_runs))

    return averages
