"""
Project Euler Problem 85: Counting rectangles

Problem:
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles.
Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

Solution Idea:
First, we need a formula to calculate the number of rectangles in an `m x n` grid.

1.  **Formula for Counting Rectangles**:
    - A rectangle is defined by two distinct horizontal lines and two distinct vertical lines.
    - In an `m x n` grid, there are `m+1` horizontal lines and `n+1` vertical lines.
    - The number of ways to choose 2 horizontal lines is `C(m+1, 2) = (m+1)*m / 2`.
    - The number of ways to choose 2 vertical lines is `C(n+1, 2) = (n+1)*n / 2`.
    - The total number of rectangles is the product of these two: `((m+1)*m / 2) * ((n+1)*n / 2)`.
    - This is the product of the `m`-th and `n`-th triangle numbers.

2.  **Search Strategy**:
    - We need to find the dimensions `(m, n)` for which the number of rectangles is closest to 2,000,000.
    - We can iterate through possible values for the width `m` and, for each `m`, find the height `n` that gives the closest result.
    - We can set a reasonable upper bound for the search. If `m=1`, the number of rectangles is `n(n+1)/2`. We can solve `n(n+1)/2 approx 2,000,000` to get `n^2 approx 4,000,000`, so `n` is around 2000. The grid dimensions will be somewhere in this ballpark. A search limit of `m` up to 2000 should be more than sufficient.

3.  **Algorithm**:
    a.  Set `target = 2,000,000`.
    b.  Initialize `closest_diff = infinity` and `result_area = 0`.
    c.  Loop `m` from 1 upwards.
    d.  For each `m`, calculate the number of ways to choose the horizontal lines: `rects_m = m * (m + 1) // 2`.
    e.  Loop `n` from `m` upwards (to avoid duplicate pairs like `(3,2)` and `(2,3)`).
    f.  For each `n`, calculate the number of ways to choose vertical lines: `rects_n = n * (n + 1) // 2`.
    g.  Calculate the total number of rectangles: `total_rects = rects_m * rects_n`.
    h.  Calculate the difference: `diff = abs(total_rects - target)`.
    i.  If `diff < closest_diff`, update `closest_diff = diff` and `result_area = m * n`.
    j.  If `total_rects` becomes much larger than the target, we can break the inner loop for `n` and move to the next `m`, as further increases in `n` will only make the count larger.
"""

def solve():
    """
    Finds the area of the rectangular grid with the number of rectangles
    closest to two million.
    """
    target = 2_000_000
    closest_diff = float('inf')
    result_area = 0

    # Set a reasonable search limit for the width 'm'.
    # If m=1, n would be ~2000. If m=n, m^2(m+1)^2/4 ~ 2M => m^4 ~ 8M => m ~ 53.
    # A limit of 100 for m should be very safe.
    limit = 100

    for m in range(1, limit):
        rects_m = m * (m + 1) // 2
        
        for n in range(m, limit * 2): # Search n in a wider range
            rects_n = n * (n + 1) // 2
            total_rects = rects_m * rects_n
            
            diff = abs(total_rects - target)
            
            if diff < closest_diff:
                closest_diff = diff
                result_area = m * n
            
            # If we've gone way past the target, we can stop for this m
            if total_rects > target + closest_diff:
                break
                
    return result_area

if __name__ == "__main__":
    print(solve())
