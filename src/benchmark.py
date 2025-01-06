import time
from typing import Callable

def benchmark(n: int, function: Callable):
    start_time = time.time()
    result = function(n)
    duration = time.time() - start_time
    return function.__name__, result, duration