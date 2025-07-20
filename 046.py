"""
Project Euler Problem 46: Goldbach's other conjecture

Problem:
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2
It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

Solution Idea:
We need to find the first odd composite number `n` that does not satisfy the equation `n = p + 2*k^2` for any prime `p` and integer `k >= 1`.

1.  **Sieve for Primes**: Since we will need to check for primality many times, it's efficient to pre-compute all primes up to a reasonable limit using a Sieve of Eratosthenes. A limit of 10,000 should be sufficient to find the first counterexample. This will give us a boolean array for O(1) primality lookups.

2.  **Iterate and Test**: We will iterate through odd numbers `n`, starting from 3, and check two things for each:
    a) Is `n` composite? We can check this using our sieve (`not is_prime[n]`).
    b) If it is an odd composite, does it satisfy the conjecture?

3.  **Checking the Conjecture**: For a given odd composite `n`, we need to see if there exists a prime `p` and an integer `k` such that `n = p + 2*k^2`.
    - We can rearrange this to `p = n - 2*k^2`.
    - We can then loop through values of `k` starting from 1.
    - For each `k`, we calculate `p_candidate = n - 2*k^2`.
    - If `p_candidate` is less than 2, we can stop checking for this `n`, as there are no smaller primes.
    - If `p_candidate` is a prime (which we can check instantly with our sieve), then `n` satisfies the conjecture. We can stop checking for this `n` and move to the next odd composite.

4.  **Finding the Counterexample**: If we go through all possible values of `k` for a given `n` and none of the resulting `p_candidate` values are prime, then we have found our counterexample. This `n` is the number we are looking for.
"""
import math

def solve():
    """
    Finds the smallest odd composite that cannot be written as the sum of a prime and twice a square.
    """
    limit = 10000  # A reasonable search limit
    
    # Sieve of Eratosthenes to find primes
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i*i, limit, i):
                is_prime[multiple] = False

    # Start checking odd numbers from 9 (the first odd composite)
    n = 9
    while True:
        if not is_prime[n]: # It's an odd composite number
            found_representation = False
            k = 1
            while True:
                twice_square = 2 * k * k
                if twice_square > n:
                    # No solution is possible for larger k
                    break
                
                p_candidate = n - twice_square
                if is_prime[p_candidate]:
                    found_representation = True
                    break # Found a representation, move to the next n
                
                k += 1
            
            if not found_representation:
                # We've checked all possible k and found no representation
                return n
        
        n += 2 # Move to the next odd number

if __name__ == "__main__":
    print(solve())
