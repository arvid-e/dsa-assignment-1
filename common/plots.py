import math
from pathlib import Path

import matplotlib.pyplot as plt

from common.linear_regression import lin_reg

ROOT = Path(__file__).resolve().parents[1]

PART1_FIGURES_DIR = ROOT / "part1" / "figures"

PART2_FIGURES_DIR = ROOT / "part2" / "figures"

FIGURES_DIR = ROOT / "figures"


def use_figures_dir(path):
    # Lets each part save its figures in its own folder
    global FIGURES_DIR
    FIGURES_DIR = Path(path)


def _save(filename):
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    path = FIGURES_DIR / filename
    plt.savefig(path)
    print(f"saved {path}")


def plot_runs(sizes, all_runs, title, filename):
    plt.figure()
    for i, measurements in enumerate(all_runs):
        plt.plot(sizes, measurements, marker='o', label=f'Run {i + 1}')

    plt.xlabel('Input size (n)')
    plt.ylabel('Execution time (s)')
    plt.title(title)
    plt.legend()
    _save(filename)


def plot_average(sizes, averages, title, filename):
    plt.figure()
    plt.plot(sizes, averages, marker='o', color='black',
             label='Average of runs')
    plt.xlabel('Input size (n)')
    plt.ylabel('Execution time (s)')
    plt.title(title)
    plt.legend()
    _save(filename)


def plot_comparison(x_values, values_by_name, xlabel, title, filename):
    plt.figure()
    for name, values in values_by_name.items():
        plt.plot(x_values, values, marker='o', label=name)

    plt.xlabel(xlabel)
    plt.ylabel('Execution time (s)')
    plt.title(title)
    plt.legend()
    _save(filename)


def plot_average_comparison(sizes, averages_by_name, title, filename):
    plot_comparison(sizes, averages_by_name, 'Input size (n)',
                    title, filename)


def plot_loglog_fit(sizes, averages, title, filename):
    log_sizes = [math.log(n) for n in sizes]
    log_times = [math.log(t) for t in averages]

    m, k = lin_reg(log_sizes, log_times)

    plt.figure()
    plt.plot(log_sizes, log_times, 'o', label='Measured data (log-log)')
    plt.plot(log_sizes, [m + k * lx for lx in log_sizes], '-',
             label=f'Fit (k={k:.3f})')
    plt.xlabel('log(n)')
    plt.ylabel('log(time)')
    plt.title(title)
    plt.legend()
    _save(filename)

    return k


def plot_loglog_comparison(sizes, averages_by_name, title, filename):
    log_sizes = [math.log(n) for n in sizes]
    ks = {}

    plt.figure()
    for name, averages in averages_by_name.items():
        log_times = [math.log(t) for t in averages]
        m, k = lin_reg(log_sizes, log_times)
        ks[name] = k

        points = plt.plot(log_sizes, log_times, 'o')
        color = points[0].get_color()
        plt.plot(log_sizes, [m + k * lx for lx in log_sizes], '-',
                 color=color, label=f'{name} (k={k:.3f})')

    plt.xlabel('log(n)')
    plt.ylabel('log(time)')
    plt.title(title)
    plt.legend()
    _save(filename)

    return ks


def plot_ratio(sizes, numerators, denominators, ylabel, title, filename):
    ratios = [a / b for a, b in zip(numerators, denominators)]

    plt.figure()
    plt.plot(sizes, ratios, marker='o', color='black')
    plt.ylim(bottom=0)
    plt.xlabel('Input size (n)')
    plt.ylabel(ylabel)
    plt.title(title)
    _save(filename)

    return ratios
