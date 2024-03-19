#!/usr/bin/python3
"""Defines minOperations"""


def minOperations(n):
    """Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Args:
        n (int): Number of H characters desired.

    Returns:
        int: Fewest number of operations needed.
        If n is impossible to achieve, return 0.
    """
    if n < 2:
        return 0

    n_times = 0
    n_max = 2

    while n > 1:
        if not n % n_max:
            n //= n_max
            n_times += n_max

        else:
            if n_max == 2:
                n_max += 1
            else:
                n_max += 2

    return n_times 
