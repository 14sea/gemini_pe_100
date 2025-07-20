"""
Project Euler Problem 72: Counting fractions

Problem:
Consider the fraction, n/d, where n and d are positive integers. If n < d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get 21 elements.

How many elements would be contained in the set of reduced proper fractions for d <= 1,000,000?

Solution Idea:
The problem asks for the total number of reduced proper fractions `n/d` where `d <= 1,000,000`.

1.  **Connection to Euler's Totient Function**:
    - For a given denominator `d`, the number of possible numerators `n` (where `1 <= n < d`) that are relatively prime to `d` (i.e., `HCF(n, d) = 1`) is exactly the definition of Euler's totient function, `phi(d)`.
    - Therefore, the total number of such fractions is the sum of `phi(d)` for all `d` from 2 to 1,000,000.
    - The problem is equivalent to calculating `sum(phi(d) for d in 2..1,000,000)`.

2.  **Efficiently Calculating `phi` values**:
    - Calculating `phi(d)` for each `d` individually by factoring it would be too slow, as this would be repeated for up to a million numbers.
    - A much more efficient method is to adapt the Sieve of Eratosthenes to calculate the `phi` values for all numbers up to the limit in one go.

3.  **Sieve for Totients**:
    a.  Create an array, `phi`, of size `limit + 1`, and initialize `phi[i] = i` for all `i`.
    b.  Iterate through numbers `p` from 2 up to the limit.
    c.  If `phi[p] == p`, it means `p` is a prime number.
    d.  When a prime `p` is found, iterate through all of its multiples `j` (from `p` up to the limit, in steps of `p`).
    e.  For each multiple `j`, update its `phi` value using the formula: `phi[j] = phi[j] * (1 - 1/p)`. This can be done with integer arithmetic as `phi[j] = phi[j] // p * (p - 1)`.

4.  **Final Summation**:
    - After the sieve has computed all the `phi` values up to 1,000,000, we simply sum the values in the `phi` array from index 2 to 1,000,000.
    - This sum will be the total count of the reduced proper fractions.
"""

def solve():
    """
    Counts the number of reduced proper fractions for d <= 1,000,000.
    This is equivalent to the sum of phi(d) for d from 2 to 1,000,000.
    """
    limit = 1_000_000
    
    # Initialize phi array where phi[i] = i
    phi = list(range(limit + 1))
    
    # Sieve to calculate totients
    for i in range(2, limit + 1):
        if phi[i] == i: # i is a prime
            # Update phi for all multiples of i
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i
                
    # The total number of fractions is the sum of phi(d) for d from 2 to limit.
    # We can sum the whole array and subtract phi[0] and phi[1].
    # phi[0] is 0, phi[1] is 1.
    return sum(phi) - 1

if __name__ == "__main__":
    print(solve())
