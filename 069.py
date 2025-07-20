"""
Project Euler Problem 69: Totient maximum

Problem:
Euler's totient function, phi(n), is defined as the number of positive integers not exceeding n which are relatively prime to n.
Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.

Solution Idea:
We need to find the number `n` that maximizes the ratio `n / phi(n)`.

1.  **Euler's Product Formula**:
    The totient function can be calculated using Euler's product formula:
    `phi(n) = n * product(1 - 1/p)` for all distinct prime factors `p` of `n`.

2.  **Maximizing the Ratio**:
    If we rearrange the formula, we get:
    `n / phi(n) = 1 / product(1 - 1/p)`
    `n / phi(n) = product(p / (p - 1))` for all distinct prime factors `p` of `n`.

    To maximize this ratio, we need to:
    a.  Include as many distinct prime factors as possible.
    b.  Use the smallest possible prime factors, because the term `p / (p - 1)` is largest for small `p`. For example, `2/(2-1) = 2`, `3/(3-1) = 1.5`, `5/(5-1) = 1.25`, etc. The value of the term gets closer to 1 as `p` increases.

3.  **The Strategy**:
    The strategy is to build a number `n` by multiplying the smallest primes together (2, 3, 5, 7, ...) until the product exceeds the limit of 1,000,000. This number, being the product of the smallest distinct primes, will have the largest possible `n / phi(n)` ratio within the given limit. This is because any other number `m < n` would either have fewer prime factors, larger prime factors, or repeated prime factors (which don't affect the ratio), all of which would result in a smaller `n / phi(n)` value.

4.  **Algorithm**:
    a.  Start with `n = 1`.
    b.  Generate a sequence of prime numbers: 2, 3, 5, 7, 11, ...
    c.  Multiply `n` by the next prime in the sequence.
    d.  If the new `n` is still within the limit of 1,000,000, continue.
    e.  If the new `n` exceeds the limit, then the previous value of `n` is our answer.
"""

def solve():
    """
    Finds the value of n <= 1,000,000 for which n/phi(n) is a maximum.
    """
    limit = 1_000_000
    
    # We need a way to get primes in order
    primes = []
    is_prime = [True] * 100 # A small sieve is enough to get the first few primes
    for p in range(2, 100):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, 100, p):
                is_prime[i] = False

    result = 1
    for p in primes:
        if result * p > limit:
            break
        result *= p
        
    return result

if __name__ == "__main__":
    print(solve())
