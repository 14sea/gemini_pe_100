"""
Project Euler Problem 73: Counting fractions in a range

Problem:
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 12,000?

Solution Idea:
This problem asks us to count the number of reduced proper fractions `n/d` that satisfy `1/3 < n/d < 1/2` with `d <= 12,000`.

1.  **Bounds for `n`**: For a given denominator `d`, we need to find the number of integers `n` such that `1/3 < n/d < 1/2`.
    - This is equivalent to `d/3 < n < d/2`.
    - So, for each `d`, `n` must be in the range `floor(d/3) + 1` to `ceil(d/2) - 1`.

2.  **Relatively Prime Condition**: We also need `HCF(n, d) = 1`.

3.  **Algorithm**:
    a.  Set a counter `count = 0`.
    b.  Iterate `d` from 1 to 12,000.
    c.  For each `d`, determine the lower and upper bounds for `n`:
        - `n_min = d // 3 + 1`
        - `n_max = (d - 1) // 2` (This is a safe way to calculate `ceil(d/2) - 1` for integers).
    d.  Iterate `n` from `n_min` to `n_max`.
    e.  For each pair `(n, d)`, check if `HCF(n, d) == 1`. We can use `math.gcd` for this.
    f.  If they are relatively prime, increment the `count`.
    g.  The final `count` is the answer.
"""
import math

def solve():
    """
    Counts the number of reduced proper fractions between 1/3 and 1/2 for d <= 12,000.
    """
    limit = 12000
    count = 0
    
    for d in range(1, limit + 1):
        n_min = d // 3 + 1
        n_max = (d - 1) // 2
        
        for n in range(n_min, n_max + 1):
            if math.gcd(n, d) == 1:
                count += 1
                
    return count

if __name__ == "__main__":
    print(solve())
