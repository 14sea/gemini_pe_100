"""
Project Euler Problem 32: Pandigital products

Problem:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

Solution Idea:
We are looking for identities of the form `a * b = c` where the concatenation of `a`, `b`, and `c` is a 1-through-9 pandigital number. This means the combined string of digits must be of length 9 and contain each digit from 1 to 9 exactly once.

1.  **Determine the possible number of digits**:
    Let `d(x)` be the number of digits in `x`. We need `d(a) + d(b) + d(c) = 9`.
    Let's analyze the possible digit counts for `a` and `b`:
    - If `a` has 1 digit and `b` has 1, 2, or 3 digits, the total number of digits will be less than 9.
    - If `a` has **1 digit** and `b` has **4 digits**, then `c` (the product) will have 4 digits. Total digits: `1 + 4 + 4 = 9`. This is a valid case.
    - If `a` has **2 digits** and `b` has **3 digits**, then `c` will have 4 digits. Total digits: `2 + 3 + 4 = 9`. This is also a valid case.
    - Any other combination (e.g., 2-digit * 4-digit) will result in more than 9 total digits.
    - Since multiplication is commutative (`a*b = b*a`), we don't need to check (4-digit * 1-digit) or (3-digit * 2-digit) separately.

2.  **Algorithm**:
    - We will use a `set` to store the products we find. This automatically handles the hint about not including duplicate products in the sum.
    - We will iterate through the two valid cases for the number of digits:
        - **Case 1**: `a` is a 1-digit number (1-9) and `b` is a 4-digit number (1000-9999).
        - **Case 2**: `a` is a 2-digit number (10-99) and `b` is a 3-digit number (100-999).
    - For each pair `(a, b)`, we calculate the product `c`.
    - We then form a string by concatenating `a`, `b`, and `c`.
    - We check if this string is 1-through-9 pandigital. A simple way to do this is to check if the length of the string is 9 and if the set of its characters is equal to the set `{'1', '2', '3', '4', '5', '6', '7', '8', '9'}`.
    - If it is pandigital, we add the product `c` to our set.

3.  **Final Sum**: After checking all possible pairs, the answer is the sum of the unique products in our set.
"""

def solve():
    """
    Finds the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital.
    """
    pandigital_products = set()
    digits = set('123456789')

    # Case 1: 1-digit * 4-digit = 4-digit product
    for a in range(1, 10):
        for b in range(1000, 10000):
            product = a * b
            s = str(a) + str(b) + str(product)
            if len(s) > 9:
                break  # Product is too large, further b's will also be too large
            if len(s) == 9 and set(s) == digits:
                pandigital_products.add(product)

    # Case 2: 2-digit * 3-digit = 4-digit product
    for a in range(10, 100):
        for b in range(100, 1000):
            product = a * b
            s = str(a) + str(b) + str(product)
            if len(s) > 9:
                break # Product is too large
            if len(s) == 9 and set(s) == digits:
                pandigital_products.add(product)

    return sum(pandigital_products)

if __name__ == "__main__":
    print(solve())
