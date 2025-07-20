"""
Project Euler Problem 60: Prime pair sets

Problem:
The primes 3, 7, 109, and 673 are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

Solution Idea:
This is a search problem for a special set of five primes. A brute-force check of all combinations of five primes would be far too slow. A more intelligent approach is to build the set of primes one by one. Since we are looking for the *lowest sum*, we should start our search with the smallest primes and build up.

1.  **Primality Testing**: We need two forms of primality testing:
    a.  A **Sieve of Eratosthenes** to efficiently generate a list of primes up to a certain limit (e.g., 10,000). These will be the candidates for our set.
    b.  A standard `is_prime` function to test the large numbers created by concatenation. Memoization (caching results) is crucial here to avoid re-testing the same large numbers.

2.  **Pair Compatibility Check**: We'll create a helper function `check_pair(p1, p2)` that takes two primes and checks if concatenating them in both orders (`p1p2` and `p2p1`) results in two new prime numbers. This check will also be memoized to avoid redundant calculations.

3.  **Search Strategy (Recursive Search / DFS)**:
    - We can think of this as finding a "clique" of size 5 in a graph where primes are nodes and an edge exists if they form a compatible pair.
    - We will implement a recursive search function that tries to build a valid set.
    - The search starts with an empty set and a list of all candidate primes.
    - In each step, it tries to add a new prime to the set, ensuring the new prime is compatible with all primes already in the set.
    - To ensure we find the lowest sum and avoid duplicate work, we only consider primes that are larger than the primes already in our set.
    - The first set of 5 that we find will be the solution, because we are always adding the smallest available primes at each step.

4.  **Exclusions**:
    - The prime `2` can be excluded because any number ending in 2 (from concatenation) will be even and thus not prime.
    - The prime `5` can be excluded because any number ending in 5 (from concatenation) will be divisible by 5.
"""
import math

# Memoization caches for performance
prime_cache = {}
pair_cache = {}

def is_prime(n):
    """
    A standard primality test with memoization.
    """
    if n in prime_cache:
        return prime_cache[n]
    if n < 2:
        prime_cache[n] = False
        return False
    if n == 2 or n == 3:
        prime_cache[n] = True
        return True
    if n % 2 == 0 or n % 3 == 0:
        prime_cache[n] = False
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            prime_cache[n] = False
            return False
    prime_cache[n] = True
    return True

def check_pair(p1, p2):
    """
    Checks if two primes form a compatible pair, with memoization.
    """
    if (p1, p2) in pair_cache:
        return pair_cache[(p1, p2)]
    
    # Concatenate and check primality in both orders
    if not is_prime(int(str(p1) + str(p2))) or not is_prime(int(str(p2) + str(p1))):
        pair_cache[(p1, p2)] = False
        return False
        
    pair_cache[(p1, p2)] = True
    return True

def find_set(current_set, candidate_primes):
    """
    Recursively searches for a set of 5 compatible primes.
    """
    if len(current_set) == 5:
        return sum(current_set)

    # Pruning: if the current sum is already larger than a known solution, stop.
    # (For the first solution, this isn't strictly necessary but is good practice).
    
    for i in range(len(candidate_primes)):
        p = candidate_primes[i]
        
        is_compatible = all(check_pair(p, existing_p) for existing_p in current_set)
        
        if is_compatible:
            new_set = current_set + [p]
            # The next candidates must be larger than the current one
            new_candidates = candidate_primes[i+1:]
            
            result = find_set(new_set, new_candidates)
            if result is not None:
                return result
                
    return None

def solve():
    """
    Finds the lowest sum for a set of five primes with the concatenation property.
    """
    # Sieve to generate initial primes. A limit of 10000 is a good starting point.
    limit = 10000
    sieve = [True] * limit
    for i in range(3, int(limit**0.5) + 1, 2):
        if sieve[i]:
            for j in range(i*i, limit, 2*i):
                sieve[j] = False
    
    # Candidate primes, excluding 2 and 5
    primes = [3] + [i for i in range(7, limit, 2) if sieve[i]]
    
    # Pre-populate the prime cache from the sieve for faster lookups
    for i in range(limit):
        prime_cache[i] = sieve[i]

    return find_set([], primes)

if __name__ == "__main__":
    print(solve())
