def py_fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    else:
        return (py_fibonacci_recursive(n-1) + py_fibonacci_recursive(n-2))

def py_fibonacci_iterative(n: int) -> int:
    n1 = 0
    n2 = 1
    for i in range(n):
        n1, n2 = n2, n1 + n2
    return n1