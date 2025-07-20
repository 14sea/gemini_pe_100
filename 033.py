"""
Project Euler Problem 33: Digit cancelling fractions

Problem:
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

Solution Idea:
We need to find all two-digit fractions `num/den` (where `num < den`) that have this "curious" property.

1.  **Iterate through all possible fractions**:
    - We'll loop through all two-digit denominators (`den`) from 11 to 99.
    - For each `den`, we'll loop through all two-digit numerators (`num`) from 10 up to `den - 1`.

2.  **Identify and check cancellation cases**:
    - For each fraction, we represent the numerator `num` as `n1 n2` and the denominator `den` as `d1 d2`.
    - We need to find a common digit between the numerator and the denominator. The problem states that trivial cases, like cancelling a '0', should be ignored.
    - There are four possible ways a digit can be "cancelled":
        a) `n1 == d1`: Check if `num/den == n2/d2`
        b) `n1 == d2`: Check if `num/den == n2/d1`
        c) `n2 == d1`: Check if `num/den == n1/d2`
        d) `n2 == d2`: Check if `num/den == n1/d1`
    - To avoid floating-point inaccuracies, we check for equality using cross-multiplication. For example, in case (a), we check if `num * d2 == den * n2`.
    - We must also ensure the new denominator is not zero.

3.  **Find the four fractions**:
    - We'll iterate and store the four fractions that satisfy the conditions.

4.  **Calculate the final product**:
    - Once we have the four fractions, we multiply their numerators together to get a final numerator.
    - We multiply their denominators together to get a final denominator.

5.  **Simplify the result**:
    - The final step is to simplify this resulting fraction to its lowest common terms. We can do this by dividing both the final numerator and the final denominator by their greatest common divisor (GCD).
    - The answer is the value of this simplified denominator.
"""
import math

def solve():
    """
    Finds the denominator of the product of the four non-trivial digit-cancelling fractions.
    """
    curious_fractions = []

    for den in range(11, 100):
        for num in range(10, den):
            n1, n2 = num // 10, num % 10
            d1, d2 = den // 10, den % 10

            # Trivial case check
            if n2 == 0 and d2 == 0:
                continue

            # Check the four cancellation cases
            # Case n2 == d1
            if n2 == d1 and d2 != 0:
                if num * d2 == den * n1:
                    curious_fractions.append((num, den))
            # Case n1 == d2
            elif n1 == d2 and d1 != 0:
                if num * d1 == den * n2:
                    curious_fractions.append((num, den))
            # Case n1 == d1
            elif n1 == d1 and d2 != 0:
                if num * d2 == den * n2:
                    curious_fractions.append((num, den))
            # Case n2 == d2
            elif n2 == d2 and d1 != 0:
                 if num * d1 == den * n1:
                    curious_fractions.append((num, den))


    # Calculate the product of the found fractions
    product_num = 1
    product_den = 1
    for n, d in curious_fractions:
        product_num *= n
        product_den *= d

    # Simplify the final fraction
    common_divisor = math.gcd(product_num, product_den)
    
    return product_den // common_divisor

if __name__ == "__main__":
    print(solve())
