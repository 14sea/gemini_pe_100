"""
Project Euler Problem 63: Powerful digit counts

Problem:
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

Solution Idea:
We are looking for the number of pairs of integers `(b, n)` where `b >= 1`, `n >= 1`, such that the number `x = b^n` has exactly `n` digits.

1.  **Formulating the Condition**:
    A number `x` has `n` digits if and only if `10^(n-1) <= x < 10^n`.
    Substituting `x = b^n`, we get the condition:
    `10^(n-1) <= b^n < 10^n`

2.  **Finding Constraints on the Base `b`**:
    Let's look at the right side of the inequality: `b^n < 10^n`. Taking the n-th root of both sides gives `b < 10`. This is a powerful constraint, as it means the base `b` can only be an integer from 1 to 9. If `b` were 10 or greater, `b^n` would always have more than `n` digits (e.g., `10^n` has `n+1` digits).

3.  **Finding Constraints on the Power `n`**:
    Now let's look at the left side: `10^(n-1) <= b^n`.
    We can take the logarithm (base 10) of both sides:
    `log10(10^(n-1)) <= log10(b^n)`
    `n - 1 <= n * log10(b)`
    `n - n * log10(b) <= 1`
    `n * (1 - log10(b)) <= 1`
    `n <= 1 / (1 - log10(b))`

    This inequality shows that for any given base `b` (from 1 to 9), there is an upper limit on the value of `n`. As `n` gets larger, `b^n` grows more slowly than `10^(n-1)`, and eventually, the number of digits in `b^n` will be less than `n`.

4.  **Algorithm**:
    - We can simply iterate through the possible bases `b` from 1 to 9.
    - For each base, we can iterate through powers `n` starting from 1.
    - In the inner loop, we check if the number of digits in `b^n` is equal to `n`.
    - If it is, we increment a counter.
    - If the number of digits becomes less than `n`, we know it will never catch up for that base (as per the logic above), so we can break the inner loop and move to the next base.
    - This process is guaranteed to terminate and will find all such numbers.
"""

def solve():
    """
    Counts how many n-digit positive integers exist which are also an nth power.
    """
    count = 0
    
    # The base 'b' must be less than 10.
    for b in range(1, 10):
        n = 1
        while True:
            power = b**n
            num_digits = len(str(power))
            
            if num_digits == n:
                count += 1
            elif num_digits < n:
                # If the number of digits drops below n, it will never catch up
                # for this base, so we can stop checking for this b.
                break
            
            # If num_digits > n, we continue to the next power.
            n += 1
            
    return count

if __name__ == "__main__":
    print(solve())
