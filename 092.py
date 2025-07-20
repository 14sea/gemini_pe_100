"""
Project Euler Problem 92: Square digit chains

Problem:
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before. Every starting number will eventually arrive at 1 or 89.
How many starting numbers below ten million will arrive at 89?

Solution Idea:
We can solve this by iterating through each number and following its chain until it reaches 1 or 89. To make this efficient, we use memoization (caching) to store the result for any number we've already computed.

1.  **Chain Calculation**: A function `sum_square_digits(n)` will compute the next number in the chain.

2.  **Memoization**: The maximum sum of squared digits for a number below 10,000,000 is for 9,999,999, which is 7 * 9^2 = 567. This means any number in a chain will quickly fall below this value. We only need a cache for numbers up to 567 to store their final destination (1 or 89).

3.  **Algorithm**:
    a.  Create a cache array `arrives_at` of size 568, initialized to 0 (unknown). Set `arrives_at[1] = 1` and `arrives_at[89] = 89`.
    b.  Initialize a counter for numbers arriving at 89.
    c.  Loop `i` from 1 to 9,999,999.
    d.  For each `i`, follow its chain.
    e.  If the current number `n` in the chain is within our cache's bounds, we can check its destination. If the destination is known, we've found the end for the starting number `i`.
    f.  If the destination is 89, increment the counter.
    g.  To make it even faster, once a chain's destination is known, we can update the cache for all intermediate numbers in the chain that are within the cache's bounds.
"""

def sum_square_digits(n):
    """Calculates the sum of the squares of the digits of n."""
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total

def solve():
    """
    Counts how many starting numbers below ten million will arrive at 89.
    """
    limit = 10_000_000
    
    # The max sum for a number under 10M is for 9,999,999 -> 7 * 9^2 = 567.
    # So we only need a cache up to this size.
    cache_size = 568
    # Use 0 as unknown, 1 for arriving at 1, 89 for arriving at 89.
    arrives_at = [0] * cache_size
    arrives_at[1] = 1
    arrives_at[89] = 89
    
    count_89 = 0
    
    for i in range(1, limit):
        n = i
        
        # Follow the chain until we reach a known endpoint
        while True:
            # If n is small enough to be in the cache and its destination is known
            if n < cache_size and arrives_at[n] != 0:
                destination = arrives_at[n]
                break
            
            # If n is not in the cache or its destination is unknown, calculate the next step
            n = sum_square_digits(n)

        if destination == 89:
            count_89 += 1
            
    return count_89

if __name__ == "__main__":
    print(solve())
