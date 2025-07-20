"""
Project Euler Problem 50: Consecutive prime sum

Problem:
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13.
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

Solution Idea:
We need to find the prime number below one million that is the sum of the longest possible sequence of consecutive primes.

1.  **Generate Primes**: First, we need a list of all prime numbers below one million. A Sieve of Eratosthenes is the most efficient method for this. We will generate both a boolean list for quick lookups (`is_prime`) and an ordered list of the prime numbers (`primes`).

2.  **Cumulative Sums**: To efficiently calculate the sum of any consecutive sequence of primes, we can pre-compute a cumulative sum (or prefix sum) array. `prime_sum[i]` will store the sum of all primes up to the `i`-th prime. The sum of primes from index `j` to `k` can then be calculated in O(1) time as `prime_sum[k+1] - prime_sum[j]`.

3.  **Search Strategy**: We want to maximize the *length* of the sequence. Therefore, the most direct approach is to iterate downwards from the longest possible sequence length.
    - First, determine the maximum possible length (`max_len`) of a sequence of consecutive primes (starting from 2) whose sum is less than one million.
    - Then, loop `length` from `max_len` down to 1.
    - For each `length`, iterate through all possible starting primes `i`.
    - Calculate the sum of the sequence of that `length` starting at `i`.
    - Check if the sum is less than one million and if the sum is a prime number.
    - Because we are iterating from the longest length downwards, the very first valid sum we find will be the answer.
"""

def solve():
    """
    Finds the prime below one million that can be written as the sum of the most consecutive primes.
    """
    limit = 1_000_000
    
    # Step 1: Sieve of Eratosthenes
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i*i, limit, i):
                is_prime[multiple] = False
    
    primes = [i for i, p in enumerate(is_prime) if p]
    
    # Step 2: Cumulative sum of primes
    prime_sum = [0] * (len(primes) + 1)
    for i in range(len(primes)):
        prime_sum[i+1] = prime_sum[i] + primes[i]
        
    # Step 3: Search for the longest sequence
    max_len = 0
    result_prime = 0
    
    # Iterate through all possible start points
    for i in range(len(primes)):
        # Iterate through all possible end points
        for j in range(i + max_len, len(primes)):
            
            current_sum = prime_sum[j] - prime_sum[i]
            
            # If the sum exceeds the limit, any further sums from this start point will also exceed it.
            if current_sum >= limit:
                break
            
            current_len = j - i
            if current_len > max_len and is_prime[current_sum]:
                max_len = current_len
                result_prime = current_sum
                
    return result_prime

if __name__ == "__main__":
    print(solve())
