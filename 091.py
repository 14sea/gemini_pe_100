"""
Project Euler Problem 91: Right triangles with integer coordinates

Problem:
The points P(x1, y1) and Q(x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form triangle OPQ.
Given that 0 <= x1, y1, x2, y2 <= 50, how many right triangles can be formed?

Solution Idea:
We need to count the number of unique triangles OPQ that have a right angle. The right angle can be at the origin (O), at point P, or at point Q. We can count these cases. A systematic way is to iterate through all possible positions for P and Q and check the condition, but that's too slow (O(N^4)).

A more efficient approach is to fix one point, say P, and then count how many other points Q can form a right triangle with OP.

1.  **Case 1: Right Angle at the Origin (O)**
    - For the angle at O to be a right angle, the line segments OP and OQ must be perpendicular. This means one point must lie on the x-axis and the other on the y-axis.
    - Let P be on the x-axis: `P(x1, 0)` where `x1` is from 1 to 50 (50 choices).
    - Let Q be on the y-axis: `Q(0, y2)` where `y2` is from 1 to 50 (50 choices).
    - This gives `50 * 50 = 2500` such triangles.

2.  **Case 2: Right Angle at a non-origin point P**
    - We can iterate through every possible point for `P(x1, y1)` in the grid (excluding the origin).
    - For each `P`, we need to find the number of points `Q(x2, y2)` such that the angle at `P` is a right angle.
    - This means the vector `PO` must be perpendicular to the vector `PQ`.
    - `PO = (-x1, -y1)`
    - `PQ = (x2 - x1, y2 - y1)`
    - Their dot product must be zero: `-x1(x2 - x1) - y1(y2 - y1) = 0`.
    - A more geometric way is to consider the line passing through P perpendicular to OP. Any point Q on this line will form a right angle at P.
    - The vector `OP` is `(x1, y1)`. A perpendicular direction vector is `(-y1, x1)`. To get all integer points on the perpendicular line, we use the primitive direction vector by dividing by the greatest common divisor: `(dx, dy) = (-y1/gcd, x1/gcd)`.
    - Any valid point `Q` can be expressed as `Q = P + k * (dx, dy)` for some integer `k`.
    - We can count how many integer values of `k` (both positive and negative) result in a point `Q` that is within the grid boundaries `[0, 50] x [0, 50]`.

3.  **Total Count**: The total number of triangles is the sum from Case 1 plus the sum from Case 2. The second case counts all triangles with a right angle at a non-origin point. Since the roles of P and Q are symmetric, by counting all possibilities for a right angle at P, we cover all such triangles exactly once.
"""
import math

def solve():
    """
    Finds the number of right triangles that can be formed with vertices
    O(0,0), P(x1, y1), Q(x2, y2) where coordinates are in [0, 50].
    """
    limit = 50
    count = 0

    # Case 1: Right angle at the origin O(0,0).
    # P must be on one axis (and not the origin), Q on the other.
    # P on x-axis: (x1, 0) where x1 in [1, 50] -> 50 choices
    # Q on y-axis: (0, y2) where y2 in [1, 50] -> 50 choices
    # Total = 50 * 50 = 2500.
    count += limit * limit

    # Case 2: Right angle at P(x1, y1).
    # We iterate through all possible points for P and count the number of
    # valid points Q that form a right angle at P.
    for x1 in range(limit + 1):
        for y1 in range(limit + 1):
            # P cannot be the origin
            if x1 == 0 and y1 == 0:
                continue

            # Vector OP is (x1, y1). A perpendicular vector is (-y1, x1).
            # To find all integer points along this perpendicular line from P,
            # we use the primitive perpendicular vector.
            common_divisor = math.gcd(x1, y1)
            dx = -y1 // common_divisor
            dy = x1 // common_divisor

            # We are looking for points Q = P + k * (dx, dy)
            # Q = (x1 + k*dx, y1 + k*dy)
            
            # Count points in the "positive" direction (k > 0)
            k = 1
            while True:
                x2 = x1 + k * dx
                y2 = y1 + k * dy
                if 0 <= x2 <= limit and 0 <= y2 <= limit:
                    count += 1
                else:
                    break
                k += 1
            
            # Count points in the "negative" direction (k < 0)
            k = -1
            while True:
                x2 = x1 + k * dx
                y2 = y1 + k * dy
                if 0 <= x2 <= limit and 0 <= y2 <= limit:
                    count += 1
                else:
                    break
                k -= 1
                
    return count

if __name__ == "__main__":
    print(solve())
