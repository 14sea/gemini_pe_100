"""
Project Euler Problem 86: Cuboid route

Problem:
A spider, S, sits in one corner of a cuboid room, and a fly, F, sits in the opposite corner. The shortest "straight line" distance from S to F is found by unfolding the cuboid. For a cuboid with dimensions L x W x H, the shortest path has a length of sqrt(L^2 + (W+H)^2), assuming L is the largest dimension.

Find the least value of M such that the number of distinct cuboids, with integer dimensions up to M x M x M, for which the shortest route has integer length, first exceeds one million.

Solution Idea:
Instead of iterating through all cuboids for a given M (O(M^3)), which is too slow, we can iterate M and count the new solutions where the largest dimension is exactly M.

1.  **Shortest Path and Pythagorean Triples**: The condition is that `L^2 + (W+H)^2` must be a perfect square. This means `L` and `(W+H)` are the two shorter sides of a Pythagorean triple.

2.  **Optimized Counting**:
    - We will loop `M` from 1 upwards, representing the largest dimension of the cuboid.
    - For each `M`, we need to find pairs `(W, H)` such that `1 <= H <= W <= M` and `M^2 + (W+H)^2` is a perfect square.
    - Let `s = W+H`. The sum `s` can range from 2 up to `2*M`.
    - We can iterate through `s` and check if `M^2 + s^2` is a perfect square.
    - If it is, we have a valid Pythagorean triple `(M, s, path)`. We then need to count how many integer pairs `(W, H)` satisfy `W+H = s` under the constraints `1 <= H <= W <= M`.
    - The constraints on `H` are `H <= W` (which implies `H <= s/2`) and `W <= M` (which implies `s-H <= M`, so `H >= s-M`).
    - For a given `(M, s)` pair, the number of valid `H` values is `(s // 2) - max(1, s - M) + 1`.

3.  **Algorithm**:
    a.  Initialize `count = 0` and `M = 0`.
    b.  Start a loop that increments `M` at each step.
    c.  Inside the loop, let `L = M`.
    d.  Iterate `s` (for `W+H`) from 2 up to `2*L`.
    e.  Check if `L^2 + s^2` is a perfect square.
    f.  If it is, calculate the number of valid `(W, H)` pairs for this `(L, s)` and add it to the total `count`.
    g.  When `count` first exceeds one million, the current value of `M` is the answer.
"""
import math

def solve():
    """
    Finds the least value of M such that the number of integer shortest path
    solutions for cuboids up to M x M x M first exceeds one million.
    """
    target = 1_000_000
    count = 0
    m = 0
    
    while count < target:
        m += 1
        # Let L = m, the largest dimension.
        # Iterate through the sum of the other two dimensions, s = W+H.
        # s can range from 2 up to 2*m.
        for s in range(2, 2 * m + 1):
            path_sq = m * m + s * s
            path = math.isqrt(path_sq)
            
            if path * path == path_sq:
                # We have a valid Pythagorean triple (m, s, path).
                # Now, count the number of ways to form s = W+H
                # with the constraint 1 <= H <= W <= m.
                
                # From H <= W and W+H=s, we get H <= s/2.
                if s <= m:
                    # If s <= m, then s-m <= 0. The lower bound for H is 1.
                    # The range for H is [1, s/2]. Number of solutions is s // 2.
                    count += s // 2
                else: # s > m
                    # From W <= m and W+H=s, we get s-H <= m, so H >= s-m.
                    # The range for H is [s-m, s/2].
                    count += (s // 2) - (s - m) + 1
                    
    return m

if __name__ == "__main__":
    print(solve())
