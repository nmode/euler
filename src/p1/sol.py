"""Solutions to problem 1 of Project Euler.

'Find the sum of all the natural number multiples of 3 or 5 below 1000.'

https://projecteuler.net/problem=1

See README.md for explanations and run.py for tests/execution times.
"""


from math import gcd


def iterv():
    """Iterative solution to problem 1.

    Iterates from 1 to 999 and sums the numbers that are multiples of 3 or 5.
    """

    return sum(n for n in range(1, 1000) if n % 3 == 0 or n % 5 == 0)


def arith():
    """Arithmetic solution to problem 1.

    See README.md for details.
    """

    return 3 * sum_of_first(333) + 5 * sum_of_first(199) - 15 * sum_of_first(66)


def gen_iterv(a, b, n):
    """General iterative solution to problem 1.

    Same as the iterative approach, but for arbitrary naturals a, b and n,
    rather than just 3, 5 and 1000, respectively.
    """

    return sum(x for x in range(1, n) if x % a == 0 or x % b == 0)


def gen_arith(a, b, n):
    """General arithmetic solution to problem 1.

    Same as the arithmetic approach, but for arbitrary naturals a, b and n,
    rather than just 3, 5 or 1000, respectively.
    """

    lcm = a * b // gcd(a, b)
    return (
        a * sum_of_first((n - 1) // a)
        + b * sum_of_first((n - 1) // b)
        - lcm * sum_of_first((n - 1) // lcm)
    )


def sum_of_first(n):
    """Returns the sum of the first n natural numbers."""

    return n * (n + 1) // 2
