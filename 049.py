"""
Project Euler Problem 49: Prime permutations

Problem:
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

Solution Idea:
We need to find a sequence of three 4-digit prime numbers that are permutations of each other and form an arithmetic sequence.

1.  **Sieve for Primes**: First, we need a list of all 4-digit prime numbers. A Sieve of Eratosthenes up to 9999 is the most efficient way to generate these.

2.  **Iterate and Search**: We will iterate through our list of 4-digit primes. For each prime `p1`, we will search for a second prime `p2` that is a permutation of `p1`.
    - To check if two numbers are permutations of each other, we can convert them to strings and check if the sorted versions of their characters are identical. For example, `sorted(str(1487))` is `['1', '4', '7', '8']`, which is the same as `sorted(str(4817))`.

3.  **Check for the Third Term**:
    - If we find such a pair `(p1, p2)` where `p2 > p1`, we can calculate the common difference `d = p2 - p1`.
    - We can then calculate the potential third term of the sequence: `p3 = p2 + d`.
    - We then need to check if `p3` meets our criteria:
        a) Is `p3` also a 4-digit number (i.e., less than 10000)?
        b) Is `p3` prime? (We can check this with our sieve).
        c) Is `p3` a permutation of `p1` and `p2`?

4.  **Find the "Other" Sequence**:
    - The problem states that there is one *other* sequence besides the one starting with 1487. We need to make sure our code finds this other one.
    - We can iterate through all possible pairs of 4-digit primes. When we find a sequence that works, we check if the first term is 1487. If it is, we ignore it and continue searching. The next valid sequence we find will be the one we're looking for.

5.  **Concatenate and Return**: Once we find the correct sequence `(p1, p2, p3)`, we concatenate their string representations to form the final 12-digit number.
"""
import itertools

def sieve(n):
    """Generate a boolean list of primes up to n using Sieve of Eratosthenes."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for multiple in range(i*i, n + 1, i):
                primes[multiple] = False
    return primes

def solve():
    """
    Finds the 12-digit number formed by concatenating the three terms of the
    other 4-digit arithmetic sequence of prime permutations.
    """
    limit = 9999
    is_prime = sieve(limit)
    
    # Get a list of all 4-digit primes
    primes_4_digit = [i for i in range(1000, limit + 1) if is_prime[i]]
    
    for i in range(len(primes_4_digit)):
        p1 = primes_4_digit[i]
        
        # The problem states we are looking for the *other* sequence
        if p1 == 1487:
            continue
            
        for j in range(i + 1, len(primes_4_digit)):
            p2 = primes_4_digit[j]
            
            # Check if p1 and p2 are permutations of each other
            if sorted(str(p1)) == sorted(str(p2)):
                # Calculate the potential third term
                diff = p2 - p1
                p3 = p2 + diff
                
                # Check if p3 is a 4-digit prime and a permutation of p1
                if p3 < 10000 and is_prime[p3] and sorted(str(p1)) == sorted(str(p3)):
                    return str(p1) + str(p2) + str(p3)

    return "Sequence not found."

if __name__ == "__main__":
    print(solve())
