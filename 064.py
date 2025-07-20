"""
Project Euler Problem 64: Odd period square roots

Problem:
All square roots are periodic when written as continued fractions.
For example, sqrt(23) = [4;(1,3,1,8)]. The block (1,3,1,8) repeats indefinitely, so the period is 4.
Exactly four continued fractions for N <= 13 have an odd period.

How many continued fractions for N <= 10000 have an odd period?

Solution Idea:
We need to calculate the period of the continued fraction for the square root of each non-square integer `N` from 2 to 10,000 and count how many of these periods are odd.

The algorithm for finding the continued fraction of `sqrt(N)` is described in the problem statement. We can generalize it. The process involves generating a sequence of integers `a_i` and a corresponding sequence of remainders. The period ends when a remainder is repeated.

Let's formalize the state at each step `i`. We need to keep track of three values, which we can call `m`, `d`, and `a`.
The general form of the fraction at each step is `(sqrt(N) + m) / d`.

1.  **Initialization**:
    - `a0` is the integer part of `sqrt(N)`. This is `floor(sqrt(N))`.
    - The first state for the periodic part is `m0 = 0`, `d0 = 1`, `a0 = floor(sqrt(N))`.

2.  **Iteration**:
    - For each step `i >= 0`, we calculate the next state `(m_{i+1}, d_{i+1}, a_{i+1})` from the current state `(m_i, d_i, a_i)`.
    - `m_{i+1} = d_i * a_i - m_i`
    - `d_{i+1} = (N - m_{i+1}^2) / d_i`
    - `a_{i+1} = floor((a0 + m_{i+1}) / d_{i+1})`

3.  **Finding the Period**:
    - The sequence of `a_i` (for `i > 0`) is the repeating part.
    - The period ends when the state `(m, d, a)` repeats. The sequence of `a_i` is guaranteed to be periodic. The period length is the number of steps it takes for the state to return to the initial state of the periodic part.
    - We can store the states `(m, d, a)` we have seen in a set or list. When we encounter a state that we've seen before, the cycle is complete, and the number of steps taken is the period length.

4.  **Main Algorithm**:
    a.  Initialize `odd_period_count = 0`.
    b.  Loop `N` from 2 to 10,000.
    c.  If `N` is a perfect square, skip it, as its square root is rational and has no continued fraction part.
    d.  For each `N`, apply the iterative algorithm described above to find the period length.
    e.  If the period length is odd, increment `odd_period_count`.
    f.  The final count is the answer.
"""
import math

def get_period_length(n):
    """
    Calculates the period length of the continued fraction of sqrt(n).
    """
    # Skip perfect squares
    if int(math.sqrt(n))**2 == n:
        return 0
        
    m = 0
    d = 1
    a0 = int(math.sqrt(n))
    a = a0
    
    period = 0
    
    # The period ends when a is 2*a0
    while a != 2 * a0:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period += 1
        
    return period

def solve():
    """
    Counts how many continued fractions for N <= 10000 have an odd period.
    """
    odd_period_count = 0
    limit = 10000
    
    for n in range(2, limit + 1):
        period = get_period_length(n)
        if period % 2 != 0:
            odd_period_count += 1
            
    return odd_period_count

if __name__ == "__main__":
    print(solve())
