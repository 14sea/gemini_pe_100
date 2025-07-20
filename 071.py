"""
Project Euler Problem 71: Ordered fractions

Problem:
By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

Solution Idea:
We are looking for a reduced proper fraction `n/d` that is as close as possible to `3/7` but still smaller than it, with the constraint that `d <= 1,000,000`.

1.  **The Goal**: We want to maximize the value of `n/d` subject to the conditions:
    a. `n/d < 3/7`
    b. `d <= 1,000,000`
    c. `n` and `d` are positive integers.
    d. `HCF(n, d) = 1`.

2.  **Maximizing the Fraction**: To maximize `n/d` so that it's just under `3/7`, we want to minimize the difference `3/7 - n/d`.
    This difference is `(3*d - 7*n) / (7*d)`.

3.  **Minimizing the Difference**: To make this difference as small as possible:
    a. The numerator, `3*d - 7*n`, must be as small as possible. Since `n` and `d` are integers, `3*d - 7*n` must be a positive integer. The smallest possible value is 1.
    b. The denominator, `7*d`, must be as large as possible. This means `d` should be as large as possible.

4.  **The Diophantine Equation**: This reduces the problem to finding a solution to the linear Diophantine equation `3*d - 7*n = 1`. Any solution to this equation automatically ensures that `HCF(n, d) = 1`.

5.  **Finding the Optimal `d`**: We need to find the largest `d <= 1,000,000` that can satisfy the equation for some integer `n`.
    - Rearranging the equation gives `3*d = 7*n + 1`, which can be expressed in modular arithmetic as `3*d ≡ 1 (mod 7)`.
    - To solve for `d`, we find the multiplicative inverse of 3 modulo 7. Since `3 * 5 = 15 ≡ 1 (mod 7)`, the inverse is 5.
    - Multiplying both sides by 5 gives `d ≡ 5 (mod 7)`.
    - So, we need the largest integer `d` less than or equal to 1,000,000 such that `d` leaves a remainder of 5 when divided by 7.

6.  **Calculation**:
    - We find that `1,000,000 mod 7 = 1`.
    - To get a number that is `≡ 5 (mod 7)`, we need to go back. `1,000,000 - 3 = 999,997`.
    - `999,997 mod 7 = 5`. This is the largest possible value for `d`.
    - Now we find the corresponding `n` using our equation: `n = (3*d - 1) / 7`.
    - `n = (3 * 999,997 - 1) / 7 = (2,999,991 - 1) / 7 = 2,999,990 / 7 = 428,570`.

7.  **The Answer**: The fraction is `428,570 / 999,997`. The problem asks for the numerator.
"""

def solve():
    """
    Finds the numerator of the fraction immediately to the left of 3/7
    in the sorted list of reduced proper fractions for d <= 1,000,000.
    """
    # We want to solve 3*d - 7*n = 1 for the largest d <= 1,000,000.
    # This is equivalent to finding the largest d where d === 5 (mod 7).
    
    limit = 1_000_000
    
    # 1,000,000 % 7 is 1.
    # To get to a number that is 5 mod 7, we subtract 3.
    # (1,000,000 - 1) is divisible by 7.
    # (1,000,000 - 2) % 7 = 6
    # (1,000,000 - 3) % 7 = 5
    d = limit - 3
    
    # Now find the corresponding numerator n
    # 7n = 3d - 1
    n = (3 * d - 1) // 7
    
    return n

if __name__ == "__main__":
    print(solve())
