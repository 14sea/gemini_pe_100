"""
Project Euler Problem 80: Square root digital expansion

Problem:
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

Solution Idea:
We need to calculate the first 100 decimal digits for the square root of each non-square number from 1 to 100, and then sum all these digits.

1.  **Avoiding Floating-Point Errors**: Standard floating-point arithmetic does not have enough precision to handle the 100 decimal digits required. We must use an integer-based approach.

2.  **Integer Scaling Method**: To find the first `d` fractional digits of `sqrt(n)`, we can calculate the integer square root of `n` scaled by a large power of 10. Specifically, we calculate `isqrt(n * 10^(2*d))`.
    - For this problem, `d = 100`. So we will calculate `isqrt(n * 10^200)`.
    - The result will be a large integer whose first `d` digits (after the integer part of the root) are the decimal digits we need.

3.  **Algorithm**:
    a.  Initialize `total_digital_sum = 0`.
    b.  Loop `n` from 1 to 100.
    c.  For each `n`, check if it is a perfect square. If `isqrt(n) * isqrt(n) == n`, then its square root is an integer, and we skip it.
    d.  If `n` is not a perfect square:
        i.   Set the required precision `d = 100`.
        ii.  Calculate the scaled target number: `target = n * (10**(2 * d))`.
        iii. Use `math.isqrt()` to find the integer square root of `target`.
        iv.  The result `sqrt_result` contains the integer part of `sqrt(n)` followed by the first 100 decimal digits.
        v.   Convert `sqrt_result` to a string.
        vi.  The first 100 digits of this string (after accounting for the integer part, which is always 1 or 2 digits for n<=100) are what we need. However, since the integer part's digits are not part of the sum, and the total number of digits in `sqrt_result` will be 101 (for n<100), we can simply sum the first 100 digits of the string representation of `sqrt_result`.
        vii. Sum the integer values of these 100 digit characters and add this sum to `total_digital_sum`.

4.  **Final Result**: The final `total_digital_sum` will be the answer.
"""
import math

def solve():
    """
    Finds the total of the digital sums of the first one hundred decimal digits
    for all irrational square roots of the first one hundred natural numbers.
    """
    total_digital_sum = 0
    num_digits = 100
    
    for n in range(1, 101):
        # Check if n is a perfect square
        root = math.isqrt(n)
        if root * root == n:
            continue # Skip perfect squares
            
        # Use integer scaling to find the digits
        # We need 100 decimal digits, so we need a total of ~101-102 digits in our result.
        # Let's use a precision of 100 digits for the fractional part.
        # The integer part for sqrt(n<100) is at most 1 digit (for n<10) or 2 digits (for n<100).
        # So we need about 102 digits total. Let's use a higher precision to be safe.
        precision = 105 
        target_number = n * (10**(2 * precision))
        sqrt_result = math.isqrt(target_number)
        
        # The result contains the integer part + the fractional part.
        # We only want the first 100 digits of the fractional part.
        # The integer part has len(str(root)) digits.
        s_sqrt_result = str(sqrt_result)
        
        # Sum the first 100 decimal digits
        # The integer part is small, so we can just sum the first 100 digits of the result string.
        # For n=2, isqrt(2*10^200) = 1414... (101 digits). Summing the first 100 gives the sum of the fractional part.
        # For n=99, isqrt(99*10^200) = 9949... (101 digits). Summing the first 100 gives the sum of the fractional part.
        current_sum = sum(int(digit) for digit in s_sqrt_result[:num_digits])
        
        total_digital_sum += current_sum
        
    return total_digital_sum

if __name__ == "__main__":
    print(solve())
