"""
Project Euler Problem 37: Truncatable primes

Problem:
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Solution Idea:
We need to find 11 primes with this special property. This requires an efficient way to check for primality and a systematic way to check the truncatable property.

1.  **Sieve of Eratosthenes**: Since we'll be checking primality for many numbers, it's best to pre-compute all primes up to a certain limit. A limit of one million is a reasonable starting point, as it's unlikely these special primes are extremely large if there are only 11 of them. We'll create a boolean array `is_prime` for O(1) primality lookups.

2.  **Iterate and Check**: We will loop through numbers, starting from 11 (as single-digit primes are excluded), up to our sieve limit. We will stop once we have found all 11 truncatable primes.

3.  **Truncation Logic**: For each number `n` that is prime, we need to check its two truncatable properties:
    -   **Left Truncation**: Convert the number to a string. Repeatedly remove the first character, convert the resulting substring back to an integer, and check if it's prime using our sieve. If any of these truncated numbers are not prime, the original number fails the test.
    -   **Right Truncation**: If the left truncation test passes, do the same for the right side. Repeatedly remove the last character and check if the resulting number is prime.

4.  **Collect and Sum**: If a number passes both tests, it's a truncatable prime. We add it to a list. Once our list contains 11 numbers, we can stop searching and compute their sum.
"""

def solve():
    """
    Finds the sum of the only eleven primes that are both truncatable from left to right and right to left.
    """
    limit = 1_000_000  # A reasonable upper bound to search within
    
    # Sieve of Eratosthenes to find all primes up to the limit
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i*i, limit, i):
                is_prime[multiple] = False

    truncatable_primes = []
    
    # Start searching from 11, as single-digit primes are excluded.
    for n in range(11, limit):
        if len(truncatable_primes) == 11:
            break # Stop once we've found all 11

        if not is_prime[n]:
            continue

        is_truncatable = True
        s = str(n)

        # Check left truncations
        for i in range(1, len(s)):
            if not is_prime[int(s[i:])]:
                is_truncatable = False
                break
        
        if not is_truncatable:
            continue

        # Check right truncations
        for i in range(1, len(s)):
            if not is_prime[int(s[:-i])]:
                is_truncatable = False
                break
        
        if is_truncatable:
            truncatable_primes.append(n)
            
    return sum(truncatable_primes)

if __name__ == "__main__":
    print(solve())
