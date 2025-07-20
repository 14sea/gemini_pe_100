"""
Project Euler Problem 70: Totient permutation

Problem:
Euler's totient function, phi(n), is used to determine the number of numbers less than or equal to n which are relatively prime to n.
phi(87109) = 79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.

Solution Idea:
We need to find `n` in the range `(1, 10^7)` that minimizes `n/phi(n)` while `phi(n)` is a permutation of `n`.

1.  **Minimizing n/phi(n)**:
    From Euler's product formula, `n/phi(n) = product(p / (p - 1))` for all distinct prime factors `p` of `n`.
    To minimize this ratio, we want the term `p / (p - 1)` to be as close to 1 as possible. This means we should use:
    a.  As few prime factors as possible.
    b.  The largest possible prime factors.

    This suggests that the optimal `n` is likely a product of two large primes. A single prime `p` would give `phi(p) = p-1`, which is unlikely to be a permutation of `p`. So, `n = p1 * p2` for two large primes `p1` and `p2` is the most promising candidate structure.

2.  **Sieve for Primes**:
    We need to find prime factors. A Sieve of Eratosthenes is the most efficient way to generate primes. Since `n = p1 * p2` and `n < 10^7`, the primes `p1` and `p2` will be roughly around `sqrt(10^7)`, which is about 3162. We can generate primes up to a slightly larger value, say 4000, to be safe.

3.  **Permutation Check**:
    A simple way to check if two numbers are permutations of each other is to convert them to strings, sort the characters, and see if the sorted strings are equal.

4.  **Algorithm**:
    a.  Generate all primes up to a reasonable limit (e.g., 4000) using a sieve.
    b.  Initialize `min_ratio = infinity` and `result_n = 0`.
    c.  Iterate through all pairs of primes `(p1, p2)` from our generated list.
    d.  Calculate their product `n = p1 * p2`.
    e.  If `n` is greater than the limit `10^7`, we can break the inner loop (and potentially the outer one) as further products will also be too large.
    f.  Calculate `phi(n)`. For `n = p1 * p2`, `phi(n) = (p1 - 1) * (p2 - 1)`.
    g.  Check if `phi(n)` is a permutation of `n`.
    h.  If it is, calculate the ratio `n / phi(n)`.
    i.  If this ratio is smaller than `min_ratio`, update `min_ratio` and `result_n`.
    j.  The final `result_n` will be the answer.
"""

def sieve(n):
    """Generate a boolean list of primes up to n."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for multiple in range(i*i, n + 1, i):
                primes[multiple] = False
    return primes

def are_permutations(n1, n2):
    """Check if two numbers are permutations of each other."""
    return sorted(str(n1)) == sorted(str(n2))

def solve():
    """
    Finds the value of n for which phi(n) is a permutation of n and n/phi(n) is a minimum.
    """
    limit = 10_000_000
    # Primes around sqrt(limit) = 3162. We can search a bit wider.
    prime_limit = 4000
    
    prime_bools = sieve(prime_limit)
    primes = [i for i, is_p in enumerate(prime_bools) if is_p]
    
    min_ratio = float('inf')
    result_n = 0
    
    # Iterate through pairs of primes
    for i in range(len(primes)):
        p1 = primes[i]
        for j in range(i, len(primes)):
            p2 = primes[j]
            n = p1 * p2
            
            if n >= limit:
                break
            
            phi_n = (p1 - 1) * (p2 - 1)
            
            if are_permutations(n, phi_n):
                ratio = n / phi_n
                if ratio < min_ratio:
                    min_ratio = ratio
                    result_n = n
                    
    return result_n

if __name__ == "__main__":
    print(solve())
