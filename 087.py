"""
Project Euler Problem 87: Prime power triples

Problem:
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28.
How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

Solution Idea:
We need to find the number of unique integers N < 50,000,000 such that N = p1^2 + p2^3 + p3^4, where p1, p2, p3 are primes.

1.  **Determine Prime Limits**: We can establish upper bounds for the primes to limit our search space.
    - p3^4 < 50,000,000  =>  p3 < 85
    - p2^3 < 50,000,000  =>  p2 < 369
    - p1^2 < 50,000,000  =>  p1 < 7072

2.  **Generate Primes**: A Sieve of Eratosthenes up to 7072 is sufficient to find all necessary primes.

3.  **Generate and Sum**:
    - Create lists of the required powers (p^2, p^3, p^4) from the list of primes.
    - Use three nested loops to iterate through all combinations of one element from each list.
    - To optimize, the loops should be ordered from the largest power (fourth) to the smallest (square). This allows us to break out of inner loops early if the partial sum already exceeds the limit.
    - Store the valid sums (those under fifty million) in a set to automatically handle duplicates.

4.  **Final Count**: The answer is the final size of the set.
"""
import math

def sieve(n):
    """Generate a list of primes up to n using Sieve of Eratosthenes."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for multiple in range(i*i, n + 1, i):
                primes[multiple] = False
    prime_numbers = [i for i, is_p in enumerate(primes) if is_p]
    return prime_numbers

def solve():
    """
    Finds how many numbers below fifty million can be expressed as the sum
    of a prime square, prime cube, and prime fourth power.
    """
    limit = 50_000_000
    
    # Determine the maximum prime needed for the sieve
    max_prime_needed = int(limit**0.5) + 1
    primes = sieve(max_prime_needed)
    
    # Generate the lists of powers
    prime_squares = [p**2 for p in primes]
    prime_cubes = [p**3 for p in primes if p**3 < limit]
    prime_fourths = [p**4 for p in primes if p**4 < limit]
    
    found_numbers = set()
    
    # Iterate through all combinations of the powers
    for f in prime_fourths:
        for c in prime_cubes:
            sum_fc = f + c
            if sum_fc >= limit:
                break # Optimization: further cubes will also exceed the limit
            
            for s in prime_squares:
                total = sum_fc + s
                if total < limit:
                    found_numbers.add(total)
                else:
                    break # Optimization: further squares will also exceed the limit
                    
    return len(found_numbers)

if __name__ == "__main__":
    print(solve())
