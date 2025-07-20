"""
Project Euler Problem 36: Double-base palindromes

Problem:
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

Solution Idea:
We need to check every number from 1 up to 999,999 to see if it meets the criteria. For each number, we'll perform two checks:
1.  Is it a palindrome in base 10?
2.  Is it a palindrome in base 2?

If a number satisfies both conditions, we add it to a running total.

1.  **Iterate**: We will loop through all numbers `n` from 1 to 999,999.

2.  **Base 10 Palindrome Check**:
    - For each number `n`, we convert it to a string.
    - We can then easily check if the string is equal to its reverse. For example, in Python, `str(n) == str(n)[::-1]`.

3.  **Base 2 Palindrome Check**:
    - If the number is a palindrome in base 10, we then proceed to check its binary representation.
    - We convert the number `n` to its binary string. Python's `bin(n)` function returns a string like `'0b101'`. We need to slice this string to remove the `'0b'` prefix (e.g., `bin(n)[2:]`).
    - We then check if this binary string is a palindrome in the same way as the base 10 check.

4.  **Summation**:
    - We initialize a sum to 0.
    - If a number passes both checks, we add it to the sum.

5.  **Final Result**: The final sum after checking all numbers up to the limit is the answer. The constraint about leading zeros is naturally handled by standard string conversions of numbers.
"""

def solve():
    """
    Finds the sum of all numbers, less than one million, which are
    palindromic in base 10 and base 2.
    """
    total_sum = 0
    limit = 1_000_000
    
    for n in range(1, limit):
        # Check for base 10 palindrome
        s10 = str(n)
        if s10 == s10[::-1]:
            # If it is, check for base 2 palindrome
            s2 = bin(n)[2:] # Remove the '0b' prefix
            if s2 == s2[::-1]:
                total_sum += n
                
    return total_sum

if __name__ == "__main__":
    print(solve())
