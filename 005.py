"""
Solves the Project Euler Problem 5.

Question:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Solution Idea:
The problem asks for the Least Common Multiple (LCM) of the numbers from 1 to 20.

We can find the LCM of a set of numbers by finding the LCM of the first two numbers, then finding the LCM of that result and the third number, and so on.

The formula to find the LCM of two numbers `a` and `b` is:
LCM(a, b) = (|a * b|) / GCD(a, b)
where GCD is the Greatest Common Divisor.

So, the algorithm is:
1. Start with a result of 1.
2. Iterate through the numbers from 1 to 20.
3. In each iteration, update the result by calculating the LCM of the current result and the current number from the loop.

To implement this, we need a function for GCD. The Euclidean algorithm is a classic and efficient way to find the GCD of two numbers.

Algorithm for GCD(a, b):
- While `b` is not zero, set `a, b` to `b, a % b`.
- The result is `a`.

With the GCD function, we can easily create an LCM function and then apply it iteratively.
"""

import math

def gcd(a, b):
    """Computes the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Computes the least common multiple of a and b."""
    # LCM(a,b) * GCD(a,b) = a * b
    return a * b // gcd(a, b) if a != 0 and b != 0 else 0

def solve():
    result = 1
    for i in range(1, 21):
        result = lcm(result, i)
    print(result)

solve()