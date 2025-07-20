"""
Solves the Project Euler Problem 7.

Question:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?

Solution Idea:
To find the 10,001st prime number, we need to generate prime numbers in sequence until we have found 10,001 of them.

The overall approach will be:
1. Initialize a counter for the number of primes found, say `count = 0`.
2. Start checking numbers for primality, starting from 2.
3. For each number, use a helper function `is_prime(n)` to determine if it's prime.
4. If the number is prime, increment our `count`.
5. Continue this process until `count` reaches 10,001.
6. The last number that was identified as prime is our answer.

For the `is_prime(n)` function, we can use an efficient trial division method:
- A number `n` is prime if it is not divisible by any number other than 1 and itself.
- We can immediately handle small cases: numbers less than or equal to 1 are not prime. 2 and 3 are prime.
- Any number divisible by 2 or 3 (that isn't 2 or 3 itself) is not prime. This check eliminates a large portion of composite numbers.
- For remaining numbers, we only need to check for divisors up to the square root of `n`.
- We can further optimize by observing that all primes greater than 3 are of the form `6k ± 1`. So, we can check divisors in steps of 6 (i.e., `i` and `i+2`), starting from `i=5`.
"""

import math

def is_prime(n):
    """Checks if a number is prime using an optimized trial division method."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve():
    count = 0
    num = 1
    while count < 10001:
        num += 1
        if is_prime(num):
            count += 1
    print(num)

solve()