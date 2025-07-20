"""
Project Euler Problem 47: Distinct primes factors

Problem:
The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:
644 = 2^2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

Solution Idea:
We need to find the first number `n` such that `n`, `n+1`, `n+2`, and `n+3` all have exactly four distinct prime factors. A brute-force approach of factoring each number individually would be slow. A much more efficient method is to pre-compute the number of distinct prime factors for all numbers up to a certain limit using a sieve-like algorithm.

1.  **Sieve to Count Distinct Prime Factors**:
    - We create an array, let's call it `factors_count`, initialized to all zeros, up to a reasonable search limit (e.g., 200,000). `factors_count[i]` will store the number of distinct prime factors of `i`.
    - We iterate through numbers `i` starting from 2.
    - If `factors_count[i]` is 0, it means `i` is a prime number.
    - When we find a prime `i`, we then iterate through all of its multiples (`j = i, 2i, 3i, ...`) up to our limit and increment their distinct prime factor count (`factors_count[j] += 1`).

2.  **Search for the Consecutive Sequence**:
    - After the sieve has populated our `factors_count` array, we can simply iterate through it to find our sequence.
    - We will loop from `n = 1` up to our limit.
    - In the loop, we check if `factors_count[n]`, `factors_count[n+1]`, `factors_count[n+2]`, and `factors_count[n+3]` are all equal to 4.
    - The first `n` that satisfies this condition is the answer.
"""

def solve():
    """
    Finds the first of four consecutive integers to have four distinct prime factors each.
    """
    limit = 200000  # A reasonable search limit, can be increased if needed.
    factors_count = [0] * limit
    
    # Sieve to count the number of distinct prime factors for each number
    for i in range(2, limit):
        if factors_count[i] == 0:  # i is a prime
            # Iterate through multiples of i and increment their factor count
            for j in range(i, limit, i):
                factors_count[j] += 1
    
    # Search for the first sequence of four consecutive numbers
    consecutive_count = 0
    for i in range(2, limit):
        if factors_count[i] == 4:
            consecutive_count += 1
        else:
            consecutive_count = 0
            
        if consecutive_count == 4:
            # We found the end of the sequence, so the start is i - 3
            return i - 3
            
    return "Not found within the limit."

if __name__ == "__main__":
    print(solve())
