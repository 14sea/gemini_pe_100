"""
Project Euler Problem 77: Prime summations

Problem:
It is possible to write ten as the sum of primes in exactly five different ways:
7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?

Solution Idea:
This is a partition problem where the parts must be prime numbers. We can solve this using dynamic programming, similar to the "coin change" problem. We need to find the smallest integer `n` for which the number of prime partitions is greater than 5000.

1.  **Generate Primes**: First, we need a list of prime numbers to use as the parts of our sum. We can generate primes up to a certain limit using a sieve. We don't know the final target number, so we can start with a reasonable limit (e.g., 100) and increase it if the answer is not found.

2.  **Dynamic Programming**:
    - We will search for the target number `n` iteratively.
    - We'll use a `ways` array, where `ways[i]` stores the number of ways to write `i` as a sum of primes.
    - The approach is similar to Problem 76:
        a.  Initialize a `ways` array with `ways[0] = 1`.
        b.  Get a list of primes up to our current search limit.
        c.  For each `prime` in our list:
        d.  For each `j` from `prime` up to our search limit:
        e.  `ways[j] = ways[j] + ways[j - prime]`.

3.  **Search Strategy**:
    - We can start with a target `n = 2` and check the number of ways.
    - We can then increment `n` one by one, calculating the number of prime partitions for each `n` until we find one where the number of ways exceeds 5000.
    - The first `n` that satisfies this condition will be our answer.

4.  **Algorithm**:
    a.  Initialize `target = 10`.
    b.  Start a `while True` loop.
    c.  Inside the loop:
        i.   Generate primes up to `target`.
        ii.  Create a `ways` array of size `target + 1`.
        iii. Calculate the number of prime partitions for all numbers up to `target` using the dynamic programming method.
        iv.  Check if `ways[target]` is greater than 5000. If it is, we have found our answer, so return `target`.
        v.   If not, increment `target` and continue the loop.
"""

def solve():
    """
    Finds the first value which can be written as the sum of primes in over
    five thousand different ways.
    """
    target = 10
    
    while True:
        # Sieve to get primes up to the current target
        primes = []
        is_prime = [True] * (target + 1)
        for p in range(2, target + 1):
            if is_prime[p]:
                primes.append(p)
                for i in range(p * p, target + 1, p):
                    is_prime[i] = False
        
        # DP to count partitions
        ways = [0] * (target + 1)
        ways[0] = 1
        
        for prime in primes:
            for j in range(prime, target + 1):
                ways[j] += ways[j - prime]
                
        # Check if the current target meets the condition
        if ways[target] > 5000:
            return target
            
        target += 1

if __name__ == "__main__":
    print(solve())
