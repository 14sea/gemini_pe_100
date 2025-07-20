"""
Project Euler Problem 76: Counting summations

Problem:
It is possible to write five as a sum in exactly six different ways:
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

Solution Idea:
This problem is asking for the number of "partitions" of the integer 100. A partition of a positive integer `n` is a way of writing `n` as a sum of positive integers. The order of the addends does not matter.

The total number of partitions of `n` is denoted by `p(n)`. The problem asks for the number of ways to write 100 as a sum of *at least two* positive integers. This is equivalent to finding the total number of partitions of 100, `p(100)`, and then subtracting 1 (to exclude the case where the sum is just the number 100 itself).

We can solve this using dynamic programming, treating it as a variation of the "coin change" problem.

1.  **Dynamic Programming Setup**:
    - We want to find the number of ways to form the sum 100.
    - The "coins" we can use are the integers `{1, 2, 3, ..., 99}`. (We don't use 100 as a part, since the sum must have at least two integers).
    - Let `ways[i]` be the number of ways to write the integer `i` as a sum of integers from our "coin" set.

2.  **Algorithm**:
    a.  Create a list `ways` of size `target + 1` (i.e., 101), and initialize all elements to 0, except for `ways[0] = 1`. `ways[0] = 1` is the base case, representing one way to make the sum 0 (by choosing no numbers).
    b.  Loop through each possible integer part (our "coin") `i` from 1 to 99.
    c.  For each `i`, loop through all target sums `j` from `i` up to 100.
    d.  Update the `ways` array: `ways[j] = ways[j] + ways[j - i]`. This means the number of ways to make sum `j` is increased by the number of ways to make the sum `j - i` (to which we can now add the part `i`).
    e.  After the loops complete, `ways[100]` will hold the total number of ways to write 100 as a sum of integers less than 100. This is exactly the number of partitions into at least two parts.
"""

def solve():
    """
    Calculates the number of ways one hundred can be written as a sum of
    at least two positive integers.
    """
    target = 100
    
    # ways[i] will store the number of ways to partition i
    ways = [0] * (target + 1)
    ways[0] = 1
    
    # The parts of the sum can be any integer from 1 to 99.
    for i in range(1, target):
        for j in range(i, target + 1):
            ways[j] += ways[j - i]
            
    return ways[target]

if __name__ == "__main__":
    print(solve())
