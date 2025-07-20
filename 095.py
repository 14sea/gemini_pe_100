"""
Project Euler Problem 95: Amicable chains

Problem:
The sum of the proper divisors of a number can form a chain. For example, 12496 -> 14288 -> ... -> 12496. This is an amicable chain.
Find the smallest member of the longest amicable chain with no element exceeding one million.

Solution Idea:
The problem requires us to find the longest amicable chain starting from numbers up to one million.

1.  **Pre-compute Divisor Sums**: The core operation is finding the sum of proper divisors. Doing this repeatedly would be slow. We can pre-compute these sums for all numbers up to the limit using a sieve-like method.

2.  **Chain Traversal**: We will iterate through each number `n` from 2 to the limit. If we haven't processed `n` yet, we start building a chain from it.
    - `n_0 = n`, `n_1 = sum_divisors(n_0)`, `n_2 = sum_divisors(n_1)`, etc.

3.  **Cycle Detection**:
    - As we build a chain, we keep track of the numbers in the current path.
    - The chain terminates if a number exceeds the limit, or if we encounter a number that has been seen before.
    - If the repeated number was part of the *current* chain, we have found a cycle.
    - If the repeated number was part of a *previous* chain (which we can track with a global `visited` array), then this chain merges with another one, and we can discard it.

4.  **Tracking the Longest Chain**:
    - When we find a valid cycle, we compare its length to the maximum length found so far.
    - If the new cycle is longer, we update the maximum length and store the smallest member of this new cycle.

5.  **Algorithm**:
    a.  Create an array `divisor_sums` up to 1,000,000 and fill it using a sieve.
    b.  Create a boolean array `visited` to mark numbers that have been part of any chain.
    c.  Loop `i` from 2 to 1,000,000.
    d.  If `i` has not been visited:
        i.   Start a new `chain` list.
        ii.  Follow the sequence, adding numbers to `chain`, until a number is repeated, exceeds the limit, or is already marked as visited.
        iii. Mark all numbers in the generated `chain` as visited.
        iv.  If a cycle was found (the repeated number is in the current `chain`), check if its length is the new maximum. If so, update the max length and the result (the minimum element in the cycle).
"""

def solve():
    """
    Finds the smallest member of the longest amicable chain with no element
    exceeding one million.
    """
    limit = 1_000_000
    
    # Step 1: Pre-compute the sum of proper divisors for all numbers up to the limit
    divisor_sums = [1] * (limit + 1)
    divisor_sums[0] = divisor_sums[1] = 0
    for i in range(2, limit // 2 + 1):
        for j in range(i * 2, limit + 1, i):
            divisor_sums[j] += i

    # Step 2: Find the longest chain
    longest_chain_len = 0
    result = -1
    
    # Keep track of numbers that have been part of any chain calculation
    visited = [False] * (limit + 1)

    for i in range(2, limit + 1):
        if visited[i]:
            continue

        chain = []
        curr = i
        
        # Generate the chain until we hit a repeat, a visited number, or go out of bounds
        while curr not in chain and curr <= limit and not visited[curr]:
            chain.append(curr)
            # Handle cases where the sum of divisors is 0 or 1, which are dead ends
            if divisor_sums[curr] <= 1:
                curr = limit + 1 # Force break
            else:
                curr = divisor_sums[curr]
        
        # Mark all nodes in the path as visited
        for node in chain:
            if node <= limit:
                visited[node] = True
            
        # Check if we found a cycle within the bounds
        if curr in chain:
            cycle_start_index = chain.index(curr)
            cycle = chain[cycle_start_index:]
            cycle_len = len(cycle)
            
            if cycle_len > longest_chain_len:
                longest_chain_len = cycle_len
                result = min(cycle)
            # If lengths are equal, we want the one with the smaller minimum member
            elif cycle_len == longest_chain_len:
                result = min(result, min(cycle))
                
    return result

if __name__ == "__main__":
    print(solve())
