def py_fibonacci_recursive(n: int) -> int:
    """Use recursion to find the value of a number in a fibonacci sequence 
    based on it's position (n).

    Args:
        n (int): The position in the fibonacci sequence.

    Returns:
        int: The value of number at the given point in the sequence.
    """
    if n <= 1:
        return n
    else:
        return (py_fibonacci_recursive(n-1) + py_fibonacci_recursive(n-2))

def py_fibonacci_iterative(n: int) -> int:
    """Use iteration to find the value of a number in a fibonacci sequence 
    based on it's position (n).

    Args:
        n (int): The position in the fibonacci sequence.

    Returns:
        int: The value of number at the given point in the sequence.
    """
    n1 = 0
    n2 = 1
    for i in range(n):
        n1, n2 = n2, n1 + n2
    return n1