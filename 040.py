"""
Project Euler Problem 40: Champernowne's constant

Problem:
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the n-th digit of the fractional part, find the value of the following expression.
d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

Solution Idea:
Generating the entire string up to the millionth digit would be inefficient. A better approach is to mathematically determine which number and which digit within that number corresponds to a given index `n`.

1.  **Identify the block of numbers**: We can determine which block of numbers (1-digit, 2-digit, 3-digit, etc.) the `n`-th digit falls into.
    -   1-digit numbers (1-9) take up `9 * 1 = 9` digits.
    -   2-digit numbers (10-99) take up `90 * 2 = 180` digits.
    -   3-digit numbers (100-999) take up `900 * 3 = 2700` digits.
    -   And so on.

2.  **Find the specific number**: Once we know the block, we can find the exact number containing the `n`-th digit. For example, to find `d_100`:
    -   It's not in the first 9 digits (from 1-digit numbers).
    -   We look for the `100 - 9 = 91`st digit within the 2-digit number block.
    -   Since each number has 2 digits, this corresponds to the `(91-1) // 2 = 45`th number (0-indexed) in this block.
    -   The first 2-digit number is 10, so the number is `10 + 45 = 55`.

3.  **Find the specific digit**:
    -   The index of the digit within the number `55` is `(91-1) % 2 = 0` (0-indexed).
    -   So, the digit is the first digit of `55`, which is `5`.

4.  **General Algorithm**: We can create a function `find_digit(n)` that implements this logic. It will loop through the blocks (1-digit, 2-digit, etc.), subtracting the total number of digits in each block from `n` until `n` falls within the current block's range. Then, it performs the calculations from steps 2 and 3 to pinpoint the exact digit.

5.  **Calculate the product**: We call this function for each required index (1, 10, 100, ...) and multiply the results together.
"""

def find_digit(n):
    """
    Finds the n-th digit in the Champernowne constant.
    """
    num_digits = 1
    count = 9
    start = 1
    
    while n > count * num_digits:
        n -= count * num_digits
        num_digits += 1
        count *= 10
        start *= 10
        
    # At this point, n is the index within the current block of numbers.
    
    # Find the number containing the digit
    # (n - 1) to make it 0-indexed
    number_index = (n - 1) // num_digits
    the_number = start + number_index
    
    # Find the digit within that number
    digit_index = (n - 1) % num_digits
    
    return int(str(the_number)[digit_index])

def solve():
    """
    Calculates the product of the specified digits of the Champernowne constant.
    """
    indices = [1, 10, 100, 1000, 10000, 100000, 1000000]
    product = 1
    
    for index in indices:
        product *= find_digit(index)
        
    return product

if __name__ == "__main__":
    print(solve())
