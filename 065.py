"""
Project Euler Problem 65: Convergents of e

Problem:
The continued fraction for e is [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ... , 1, 2k, 1, ...].
Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

Solution Idea:
We need to calculate the 100th convergent fraction, which will have a very large numerator and denominator. This requires using a method that can handle large numbers, like Python's arbitrary-precision integers.

1.  **Generate the Sequence of Terms**: First, we need to generate the sequence of terms `a_0, a_1, a_2, ...` for the continued fraction of `e`.
    - `a_0` is 2.
    - The repeating pattern for `a_i` (where `i >= 1`) is `1, 2k, 1`.
    - We can generate a list of the first 100 terms (`a_0` to `a_99`) based on this pattern.

2.  **Calculate the Convergent**: A continued fraction `[a_0; a_1, a_2, ..., a_n]` can be calculated iteratively from the inside out.
    - Let the n-th convergent be `N_n / D_n`.
    - The recurrence relation for the numerators and denominators is:
        - `N_k = a_k * N_{k-1} + N_{k-2}`
        - `D_k = a_k * D_{k-1} + D_{k-2}`
    - We need to define the initial values. Let's set `N_{-2}=0, D_{-2}=1` and `N_{-1}=1, D_{-1}=0`.
    - Then:
        - `N_0 = a_0 * N_{-1} + N_{-2} = a_0 * 1 + 0 = a_0`
        - `D_0 = a_0 * D_{-1} + D_{-2} = a_0 * 0 + 1 = 1`
        - This gives the first convergent `a_0/1`.
        - `N_1 = a_1 * N_0 + N_{-1} = a_1 * a_0 + 1`
        - `D_1 = a_1 * D_0 + D_{-1} = a_1 * 1 + 0 = a_1`
        - This gives the second convergent `(a_1*a_0 + 1) / a_1`.
    - This recurrence relation allows us to build up to the 100th convergent without complex fraction manipulation.

3.  **Algorithm**:
    a.  Generate the list of the first 100 terms (`a_0` to `a_99`) for `e`.
    b.  Initialize the numerators and denominators for the recurrence: `n_prev = 1`, `n_curr = a_0`. (We can simplify the recurrence to only need the previous two terms).
    c.  Loop from the second term (`a_1`) to the 100th term (`a_99`).
    d.  In each step, calculate the next numerator using the recurrence: `n_next = a_k * n_curr + n_prev`.
    e.  Update `n_prev = n_curr` and `n_curr = n_next`.
    f.  After the loop, `n_curr` will hold the numerator of the 100th convergent.
    g.  Calculate the sum of the digits of this final numerator.

4.  **Digital Sum**: To get the sum of the digits, we convert the final large numerator to a string and sum the integer value of each character.
"""

def solve():
    """
    Finds the sum of digits in the numerator of the 100th convergent of e.
    """
    # Step 1: Generate the sequence of terms for e's continued fraction
    # We need 100 terms for the 100th convergent (a_0 to a_99)
    terms = [2]
    k = 1
    while len(terms) < 100:
        terms.extend([1, 2 * k, 1])
        k += 1
    # Ensure we only have 100 terms
    terms = terms[:100]

    # Step 2: Calculate the numerator of the 100th convergent
    # We work backwards from the 99th term (the 100th term in the sequence)
    # The last fraction is 1 / a_99
    num = 1
    den = terms[99]
    
    # Loop backwards from a_98 down to a_0
    for i in range(98, -1, -1):
        # The new fraction is a_i + (num / den)
        # which is (a_i * den + num) / den
        # We then take the reciprocal for the next step
        new_num = terms[i] * den + num
        new_den = den
        
        # The new num/den for the next iteration is the reciprocal of this
        num = new_den
        den = new_num
        
    # After the loop, the final fraction is den/num (since we did one last flip)
    # The numerator of the final convergent is den.
    final_numerator = den
    
    # Step 3: Calculate the sum of the digits
    return sum(int(digit) for digit in str(final_numerator))

if __name__ == "__main__":
    print(solve())
