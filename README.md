# 1DV018 Assignment 1

Timing experiments for 3-sum (part 1) and sorting algorithms (part 2).

## Requirements

- Python 3.12
- matplotlib (`pip install matplotlib`)

## Running the experiments

Run every command from the repository root (this folder).

Run all experiments:

```sh
python3 run_experiments.py
```

Run only some of them by name:

```sh
python3 run_experiments.py threesum_correctness compare_all
```

Each experiment can also be run on its own as a module. Use `-m` with a
dotted path. Running the file by its path (`python3 part1/.../main.py`)
does not work, because the imports start from the repository root.

| Name                    | Module command                                          | What it does                                    |
|-------------------------|---------------------------------------------------------|-------------------------------------------------|
| `threesum_correctness`  | `python3 -m part1.threesum.correctness`                 | Checks that both 3-sum versions agree on small lists |
| `threesum_bruteforce`   | `python3 -m part1.threesum.bruteforce.main`             | Times brute-force 3-sum                         |
| `threesum_two_pointers` | `python3 -m part1.threesum.two_pointers.main`           | Times two-pointer 3-sum                         |
| `bubble_sort`           | `python3 -m part2.sorting_algorithms.bubble_sort.main`  | Times bubble sort                               |
| `insertion_sort`        | `python3 -m part2.sorting_algorithms.insertion_sort.main` | Times insertion sort                          |
| `selection_sort`        | `python3 -m part2.sorting_algorithms.selection_sort.main` | Times selection sort                          |
| `compare_simple_sorts`  | `python3 -m part2.sorting_algorithms.compare`           | Compares bubble, insertion and selection sort   |
| `compare_merge_quick`   | `python3 -m part2.sorting_algorithms.compare_merge_quick` | Compares merge sort and quick sort            |
| `compare_bucket_radix`  | `python3 -m part2.sorting_algorithms.compare_bucket_radix` | Compares bucket sort and radix sort          |
| `compare_digits`        | `python3 -m part2.sorting_algorithms.compare_digits`    | Bucket vs radix sort as the number of digits grows |
| `compare_all`           | `python3 -m part2.sorting_algorithms.compare_all`       | Compares bucket, radix, merge and quick sort    |

## Output

Results are printed to the terminal. Figures are saved as PNG files:

- Part 1: `figures/`
- Part 2: `part2/figures/`
