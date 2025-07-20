def solve():
    """
    Solves the Project Euler Problem 14.

    Question:
    The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1.

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?
    NOTE: Once the chain starts the terms are allowed to go above one million.

    Solution Idea:
    We can iterate through all numbers from 1 to 999,999 and for each number,
    we compute the length of its Collatz sequence. We keep track of the
    starting number that produces the longest chain.

    To optimize this process, we use memoization (caching) to store the
    lengths of chains that have already been calculated. This avoids
    redundant calculations for sub-sequences.
    """
    limit = 1000000
    cache = {1: 1}
    max_len = 0
    start_num = 0

    for i in range(1, limit):
        n = i
        length = 0
        while n not in cache:
            length += 1
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
        
        total_len = length + cache[n]
        cache[i] = total_len

        if total_len > max_len:
            max_len = total_len
            start_num = i
            
    print(f"The starting number under {limit} that produces the longest chain is: {start_num}")
    print(f"The length of the chain is: {max_len}")

solve()