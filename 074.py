"""
Project Euler Problem 74: Digit factorial chains

Problem:
The number 145 is well known for the property that the sum of the factorial of its digits is 1! + 4! + 5! = 145.
It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example:
69 -> 363600 -> 1454 -> 169 -> 363601 -> 1454 (loop)
Starting with 69 produces a chain of five non-repeating terms.

The longest non-repeating chain with a starting number below one million is sixty terms.
How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

Solution Idea:
We need to generate the digit factorial chain for every number from 1 to 999,999 and find how many of them have exactly 60 non-repeating terms.

1.  **Pre-compute Factorials**: The first step is to pre-compute the factorials of the digits 0-9 to avoid recalculating them constantly.

2.  **Chain Generation and Length Calculation**:
    - We need a function that takes a starting number `n` and calculates the length of its non-repeating chain.
    - To do this, we generate the sequence `n_0, n_1, n_2, ...` where `n_{i+1}` is the sum of the factorials of the digits of `n_i`.
    - We must keep track of the numbers we've seen in the current chain to detect when we enter a loop. A `set` is efficient for this.
    - The length of the non-repeating part of the chain is the number of unique terms we generate before a term repeats.

3.  **Memoization/Caching**:
    - Many chains will merge. For example, the chain for 69 merges with the chain for 1454.
    - We can significantly speed up the process by caching the length of chains we have already computed.
    - We can use a dictionary or an array `chain_lengths` to store the length of the chain starting at a number `n`.
    - When generating a new chain, if we encounter a number that is already in our cache, we can stop and add its known chain length to our current chain's length.

4.  **Algorithm**:
    a.  Pre-compute factorials `0!` through `9!`.
    b.  Initialize a cache `chain_lengths` to store computed results.
    c.  Initialize a counter `count_60 = 0`.
    d.  Loop `n` from 1 to 999,999.
    e.  For each `n`, calculate its chain length using the caching strategy.
        i.   Start a new chain sequence and a set to track terms in the *current* path.
        ii.  While the current number is not in our main `chain_lengths` cache:
             - Add it to the current path set.
             - Calculate the next number in the sequence.
        iii. Once we hit a cached number, we can determine the length of the new path and update the cache for all numbers in that path.
    f.  If the calculated chain length for `n` is 60, increment `count_60`.
    g.  The final `count_60` is the answer.
"""

# Pre-compute factorials for digits 0-9
FACTORIALS = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def sum_digit_factorials(n):
    """Calculates the sum of the factorials of the digits of n."""
    s = 0
    while n > 0:
        s += FACTORIALS[n % 10]
        n //= 10
    return s

# Cache to store the length of chains
chain_lengths = {}

def get_chain_length(n):
    """Calculates the length of the digit factorial chain starting at n, using a cache."""
    if n in chain_lengths:
        return chain_lengths[n]

    path = []
    curr = n
    while curr not in chain_lengths:
        if curr in path: # Cycle detected within the current path
            cycle_start_index = path.index(curr)
            cycle_len = len(path) - cycle_start_index
            # Update cache for all nodes in the cycle
            for i in range(cycle_start_index, len(path)):
                chain_lengths[path[i]] = cycle_len
            # Update cache for nodes before the cycle
            for i in range(cycle_start_index):
                chain_lengths[path[i]] = (cycle_start_index - i) + cycle_len
            return chain_lengths[n]
            
        path.append(curr)
        curr = sum_digit_factorials(curr)

    # We've hit a number with a known chain length
    path_len = len(path)
    cached_len = chain_lengths[curr]
    
    # Update cache for all nodes in the path we just traversed
    for i in range(path_len):
        chain_lengths[path[i]] = (path_len - i) + cached_len
        
    return chain_lengths[n]

def solve():
    """
    Finds the number of digit factorial chains with exactly 60 non-repeating terms.
    """
    limit = 1_000_000
    count_60 = 0
    
    # Pre-populate the known loops
    chain_lengths[169] = 3
    chain_lengths[363601] = 3
    chain_lengths[1454] = 3
    chain_lengths[871] = 2
    chain_lengths[45361] = 2
    chain_lengths[872] = 2
    chain_lengths[45362] = 2
    chain_lengths[145] = 1
    chain_lengths[1] = 1
    chain_lengths[2] = 1
    chain_lengths[40585] = 1


    for i in range(1, limit):
        if get_chain_length(i) == 60:
            count_60 += 1
            
    return count_60

if __name__ == "__main__":
    print(solve())
