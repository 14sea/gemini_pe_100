"""
Project Euler Problem 53: Combinatoric selections

Problem:
There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, C(5, 3) = 10.
In general, C(n, r) = n! / (r!(n−r)!), where r <= n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: C(23, 10) = 1144066.

How many, not necessarily distinct, values of C(n, r) for 1 <= n <= 100, are greater than one-million?

Solution Idea:
We need to calculate `C(n, r)` for `1 <= n <= 100` and `1 <= r <= n` and count how many of these values are greater than one million.

1.  **Direct Calculation**: A naive approach would be to calculate the factorials for `n!`, `r!`, and `(n-r)!` and then perform the division. However, `100!` is an enormous number, and we would run into precision issues or overflow with standard data types, although Python's arbitrary-precision integers can handle it.

2.  **Iterative Calculation (Pascal's Triangle)**: A more stable and efficient way to calculate `C(n, r)` is to use the relationship `C(n, r) = C(n, r-1) * (n - r + 1) / r`.
    - For a fixed `n`, we know `C(n, 0) = 1`.
    - We can then calculate `C(n, 1) = C(n, 0) * (n - 0) / 1 = n`.
    - Then `C(n, 2) = C(n, 1) * (n - 1) / 2`, and so on.
    - This avoids dealing with very large intermediate factorial numbers.

3.  **Algorithm**:
    a.  Initialize a `count = 0`.
    b.  Loop `n` from 1 to 100.
    c.  For each `n`, loop `r` from 1 to `n`.
    d.  Inside the inner loop, calculate `C(n, r)` using the iterative method described above.
    e.  Check if the calculated value of `C(n, r)` is greater than 1,000,000.
    f.  If it is, increment our `count`.

4.  **Symmetry Optimization**: We know that `C(n, r) = C(n, n-r)`. The values of `C(n, r)` for a fixed `n` increase as `r` goes from 0 to `n/2` and then decrease symmetrically.
    - This means that if we find a value `C(n, r)` that is greater than one million, then `C(n, n-r)` will also be greater than one million.
    - Furthermore, all values between `r` and `n-r` will also be greater than one million.
    - We can modify the algorithm: For each `n`, loop `r` from 1 up to `n/2`. If we find an `r` where `C(n, r) > 1,000,000`, we know that all values from `r` up to `n-r` will also exceed the limit. The number of such values is `(n - r) - r + 1 = n - 2r + 1`. We can add this number to our total count and break the inner loop for the current `n`, moving to `n+1`.
"""

def solve():
    """
    Counts how many values of C(n, r) for 1 <= n <= 100 are greater than one-million.
    """
    limit = 1_000_000
    count = 0
    
    for n in range(1, 101):
        # We can use the iterative formula C(n, r) = C(n, r-1) * (n - r + 1) / r
        # C(n, 0) is 1
        c_n_r = 1
        for r in range(1, n + 1):
            c_n_r = c_n_r * (n - r + 1) // r
            
            if c_n_r > limit:
                # Due to symmetry, all values from r to n-r will also be > limit.
                # The number of such values is (n-r) - r + 1 = n - 2r + 1
                count += (n - r) - r + 1
                break # Move to the next n
                
    return count

if __name__ == "__main__":
    print(solve())
