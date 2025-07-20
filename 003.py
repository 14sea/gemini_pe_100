"""
Solves the Project Euler Problem 3.

Question:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

Solution Idea:
To find the largest prime factor of a number, we can use a trial division method.
We start with the smallest prime number, 2, and check if it divides the given number.
If it does, we divide the number by 2 and repeat the process.
If it doesn't, we move to the next potential divisor (3, 4, 5, ...).

We can optimize this by realizing a few things:
1. We only need to check for divisors up to the square root of the current number.
   If we find a divisor larger than the square root, the other factor must be smaller, and we would have already found it.
2. When we find a divisor `d`, we should repeatedly divide the number `n` by `d` until it's no longer divisible. This ensures we remove all instances of that prime factor.
3. The final value of `n` after the loop will be the largest prime factor.
   This is because we have systematically removed all smaller prime factors. If the remaining `n` were composite, it would have a prime factor smaller than or equal to its square root, which would have already been found and divided out.
"""

def solve():
    n = 600851475143
    d = 2
    while d * d <= n:
        if n % d == 0:
            n //= d
        else:
            d += 1
    print(n)

solve()