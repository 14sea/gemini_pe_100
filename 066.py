"""
Project Euler Problem 66: Diophantine equation

Problem:
Consider quadratic Diophantine equations of the form: x^2 - Dy^2 = 1.
This is known as Pell's equation.
For example, when D=13, the minimal solution in x is 649^2 - 13 * 180^2 = 1.
It can be assumed that there are no solutions in positive integers when D is square.

Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.

Solution Idea:
The minimal solutions to Pell's equation, `x^2 - Dy^2 = 1`, are closely related to the continued fraction expansion of `sqrt(D)`.

1.  **Continued Fractions**: The fundamental solution `(x, y)` can be found from the convergents of the continued fraction of `sqrt(D)`.
    - Let the continued fraction be `[a0; a1, a2, ...]`.
    - The convergents `h_i / k_i` can be calculated using the recurrence relations:
        - `h_i = a_i * h_{i-1} + h_{i-2}`
        - `k_i = a_i * k_{i-1} + k_{i-2}`
    - With initial values `h_{-1}=1, k_{-1}=0` and `h_{0}=a0, k_{0}=1`.

2.  **Finding the Solution**:
    - We generate the terms `a_i` of the continued fraction and the corresponding convergents `h_i / k_i` one by one.
    - For each convergent, we test if `h_i^2 - D * k_i^2 == 1`.
    - The first convergent that satisfies this equation gives the minimal solution `x = h_i`.

3.  **Algorithm**:
    a.  Initialize `max_x = 0` and `result_D = 0`.
    b.  Loop `D` from 2 to 1000.
    c.  If `D` is a perfect square, skip it.
    d.  For each `D`, we will find the minimal solution `x`.
        i.  Initialize the state for the continued fraction generation: `m=0, d=1, a0=floor(sqrt(D))`.
        ii. Initialize the convergents: `h_prev=1, k_prev=0`, `h_curr=a0, k_curr=1`.
        iii.Check if the first convergent is a solution: `h_curr^2 - D * k_curr^2 == 1`.
        iv. If not, enter a loop to generate subsequent terms `a_i` and convergents until a solution is found.
    e.  Once the minimal `x` for `D` is found, compare it with `max_x`. If it's larger, update `max_x` and set `result_D = D`.
    f.  The final `result_D` is the answer.
"""
import math

def solve():
    """
    Finds the value of D <= 1000 for which the largest minimal x is obtained.
    """
    max_x = 0
    result_D = 0
    
    for D in range(2, 1001):
        # Skip perfect squares
        limit = int(math.sqrt(D))
        if limit * limit == D:
            continue
            
        # Initialize continued fraction state
        m = 0
        d = 1
        a0 = limit
        a = a0
        
        # Initialize convergents
        h_prev = 1
        h_curr = a0
        k_prev = 0
        k_curr = 1
        
        # Loop until we find a solution to Pell's equation
        while h_curr*h_curr - D * k_curr*k_curr != 1:
            # Calculate next term in continued fraction
            m = d * a - m
            d = (D - m * m) // d
            a = (a0 + m) // d
            
            # Calculate next convergent
            h_next = a * h_curr + h_prev
            k_next = a * k_curr + k_prev
            
            h_prev, h_curr = h_curr, h_next
            k_prev, k_curr = k_curr, k_next
            
        x = h_curr
        
        if x > max_x:
            max_x = x
            result_D = D
            
    return result_D

if __name__ == "__main__":
    print(solve())