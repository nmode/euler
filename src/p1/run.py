"""Tests and execution times for solutions to problem 1 of Project Euler.

See sol.py for solutions and README.md for explanations.
"""


from time import process_time
from sol import iterv, arith, gen_iterv, gen_arith


if __name__ == "__main__":
    assert (
        iterv() == arith() == gen_iterv(3, 5, 1000) == gen_arith(3, 5, 1000) == 233168
    )

    print("Answer to problem 1: 233168\n")

    for solution in [iterv, arith]:
        start = process_time()
        solution()
        end = process_time() - start

        print(f"Solution {solution.__name__} executed in {start - end}")
