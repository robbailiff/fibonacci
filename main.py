import time
from tabulate import tabulate

from src.benchmark import benchmark
from src.utils import get_args

from src.fibonacci import (
    py_fibonacci_iterative,
    py_fibonacci_recursive
)

from rust_fibonacci import (
    rust_fibonacci_iterative,
    rust_fibonacci_recursive
)

functions_to_test = [
    py_fibonacci_iterative,
    py_fibonacci_recursive,
    rust_fibonacci_iterative,
    rust_fibonacci_recursive
]

def run():
    """
    Run the program by iterating over a list of input functions and display
    the results in a table sorted by shortest execution duration.
    """
    args = get_args()
    
    print("Program starting...")
    start_time = time.time()

    results = []
    for func in functions_to_test:
        n = args.num
        name, result, duration = benchmark(n, func)
        results.append((name, result, duration))
    
    results_sorted = sorted(results, key=lambda x: x[2])

    result_table = tabulate(results_sorted, headers=["Function", "Result", "Time (s)"], floatfmt=".6f")
    print(f"\n{result_table}\n")
    
    total_duration = time.time() - start_time
    print(f"Program finished. Total Time Elapsed: {total_duration:.6f}s")

if __name__ == "__main__":
    run()
