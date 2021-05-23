# Problem 1
## Find the sum of all the natural number multiples of 3 or 5 below 1000.

### Iterative Solution
This is the trivial approach, where we iterate through 1, 2, ..., 999.
At each step, if the number is a multiple of 3 or 5, we simply add it to the sum.

The general version of this solution runs in **linear time**, as we must iterate from 1 to n-1 (in this problem, n = 1000).

Despite having a looser upper bound than the general arithmetic solution below,
this is still expected to run faster for small enough n.

### Arithmetic Solution
In this approach, we take advantage of the fact that:

<img src="https://render.githubusercontent.com/render/math?math=1 %2B 2 %2B 3 %2B ... %2B n  = \frac{n(n %2B 1)}{2}">

Notice that:

<img src="https://render.githubusercontent.com/render/math?math=3 %2B 6 %2B 9 %2B ... %2B 999 = 3(1 %2B 2 %2B 3 %2B ... %2B 333) = 3 \cdot \frac{333 \cdot 334}{2}">

Similarly:

<img src="https://render.githubusercontent.com/render/math?math=5 %2B 10 %2B 15 %2B ... %2B 995 = 5(1 %2B 2 %2B 3 %2B ... %2B 199) = 5 \cdot \frac{199 \cdot 200}{2}">

However, some numbers are multiples of both 3 and 5.
These numbers must be multiples of their least common multiple, which is 15.
Thus, after adding the two sums above, we must avoid double counting by subtracting:

<img src="https://render.githubusercontent.com/render/math?math=15 %2B 30 %2B 45 %2B ... %2B 66 = 15(1 %2B 2 %2B 3 %2B ... %2B 66) = 15 \cdot \frac{66 \cdot 67}{2}">

The final answer is then:

<img src="https://render.githubusercontent.com/render/math?math=3 \cdot \frac{333 \cdot 334}{2} %2B 5 \cdot \frac{199 \cdot 200}{2} - 15 \cdot \frac{66 \cdot 67}{2} = 233168">

Assuming fixed-bit integers, this solution runs in **constant time**.

In the worst case, the general version of this solution,
taking arbitrary inputs a and b (3 and 5 in this problem), runs in:

<img src="https://render.githubusercontent.com/render/math?math=\mathcal{O}(\log{} c), c = \min{(a, b)}">

This is due to the [upper bound of the Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm#Worst-case),
which can be used to find the least common multiple efficiently:

<img src="https://render.githubusercontent.com/render/math?math=\lcm{(a, b) = \frac{a \cdot b}{\gcd{(a, b)}}}">

For large enough n (1000 in this problem), this is expected to run faster than the general iterative solution above.
