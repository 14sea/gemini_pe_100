"""
Project Euler Problem 48: Self powers

Problem:
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

Solution Idea:
We need to find the sum of `n^n` for `n` from 1 to 1000. Calculating the full values of these numbers and then summing them would result in an astronomically large number that would be very slow to compute and difficult to store.

The key is that we only need the *last ten digits* of the final sum. This is a classic application of modular arithmetic.

1.  **Modular Arithmetic**: Finding the last ten digits of a number is equivalent to finding the number modulo `10^10`.
    - The property `(a + b) mod m = ((a mod m) + (b mod m)) mod m` allows us to compute the sum term by term, keeping the intermediate results small.
    - The property `(a * b) mod m = ((a mod m) * (b mod m)) mod m` allows us to compute the powers `n^n` efficiently without calculating the full, large number.

2.  **Modular Exponentiation**: We need to calculate `n^n mod 10^10` for each `n` from 1 to 1000. A naive loop to multiply `n` by itself `n` times would be too slow for large `n`. A much more efficient method is **modular exponentiation** (also known as exponentiation by squaring).
    - Python's built-in `pow(base, exp, mod)` function implements this very efficiently.

3.  **Algorithm**:
    - Define the modulus `m = 10**10`.
    - Initialize a total sum `total_sum = 0`.
    - Loop `n` from 1 to 1000.
    - For each `n`, calculate `term = pow(n, n, m)`.
    - Add this term to our running sum: `total_sum = (total_sum + term) % m`.
    - After the loop finishes, `total_sum` will hold the last ten digits of the series.
"""

def solve():
    """
    Finds the last ten digits of the series, 1^1 + 2^2 + ... + 1000^1000.
    """
    modulus = 10**10
    total_sum = 0
    
    for n in range(1, 1001):
        # Use Python's built-in pow(base, exp, mod) for efficient modular exponentiation
        term = pow(n, n, modulus)
        total_sum = (total_sum + term) % modulus
        
    return total_sum

if __name__ == "__main__":
    print(solve())
