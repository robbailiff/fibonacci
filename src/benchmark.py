import time
from typing import Callable, Tuple

def benchmark(function: Callable, num: int) -> Tuple[str, int, float]:
    """Measure the time taken for a given function to execute.

    Args:
        function (Callable): The function to be tested
        num (int): The number value passed to the function as an argument.

    Returns:
        Tuple[str, int, float]: The function name, function return value 
            and the execution duration.
    """
    start_time = time.time()
    result = function(num)
    duration = time.time() - start_time
    return function.__name__, result, duration
