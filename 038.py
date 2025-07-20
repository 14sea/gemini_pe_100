"""
Project Euler Problem 38: Pandigital multiples

Problem:
Take the number 192 and multiply it by each of 1, 2, and 3:
192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3).

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ..., n) where n > 1?

Solution Idea:
We are looking for the largest 9-digit number formed by concatenating `x*1, x*2, ..., x*n` that is 1-to-9 pandigital.

1.  **Determine the search range for `x`**:
    - The concatenated number must have 9 digits.
    - The integer `x` must be multiplied by `(1, 2, ..., n)` where `n` is at least 2.
    - If `x` has 5 digits (e.g., 10000), then `x*1` and `x*2` together will have at least 10 digits (`10000` and `20000`). This is too long.
    - Therefore, `x` must have at most 4 digits. A safe upper bound for our search for `x` is 9999.

2.  **Algorithm**:
    - We want to find the largest pandigital number. Such a number is likely to start with the digit '9'. This suggests that the integer `x` should also start with '9' to maximize the resulting number. However, a simple iteration is fast enough.
    - We will iterate through all possible integers `x` from 1 up to 9999.
    - For each `x`, we will build the concatenated product string by multiplying `x` by `n = 1, 2, 3, ...` and appending the results.
    - We stop appending when the concatenated string has a length of 9 or more.
    - Once we have a string, we check if it meets three conditions:
        a) Its length is exactly 9.
        b) The integer `n` used to generate it was greater than 1.
        c) It is pandigital (contains all digits from 1 to 9 exactly once).
    - We keep track of the largest number found that satisfies these conditions.

3.  **Pandigital Check**:
    - An efficient way to check if a 9-digit string is pandigital is to convert it to a set of characters and check if this set is equal to `{'1', '2', '3', '4', '5', '6', '7', '8', '9'}`.
"""

def solve():
    """
    Finds the largest 1 to 9 pandigital 9-digit number that can be formed
    as the concatenated product of an integer with (1,2, ..., n) where n > 1.
    """
    largest_pandigital = 0
    pandigital_digits = set('123456789')

    # x must be less than 10000.
    for x in range(1, 10000):
        concatenated_product = ""
        n = 1
        while len(concatenated_product) < 9:
            product = x * n
            concatenated_product += str(product)
            n += 1
        
        # Check if the resulting number is a 9-digit pandigital number.
        # The multiplier n must be greater than 1, which means our final n (which is 1 greater) must be > 2.
        if len(concatenated_product) == 9 and n > 2:
            if set(concatenated_product) == pandigital_digits:
                num = int(concatenated_product)
                if num > largest_pandigital:
                    largest_pandigital = num
                    
    return largest_pandigital

if __name__ == "__main__":
    print(solve())
