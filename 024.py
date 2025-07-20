"""
Project Euler Problem 24: Lexicographic permutations

Problem:
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Solution Idea:
Instead of generating all 10! (3,628,800) permutations, which would be inefficient, we can determine the digits of the millionth permutation one by one, from left to right. This method is based on a number system called factoradic.

1.  We are looking for the 1,000,000th permutation. In programming, it's easier to work with 0-based indices, so we'll look for the permutation at index `999,999`.

2.  There are 10 digits (0-9). The number of permutations of these 10 digits is 10!. If we fix the first digit, there are 9! permutations of the remaining 9 digits.
    - The first 9! permutations start with '0'.
    - The next 9! permutations start with '1'.
    - And so on.

3.  To find the first digit, we can see which block of 9! permutations our target index falls into.
    - `999,999 / 9! = 999,999 / 362,880 = 2` (integer division).
    - This means the first digit is the digit at index 2 of our available digits `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, which is '2'.

4.  Now we need to find which permutation we're looking for within that block. We update our target index by taking the remainder:
    - `999,999 % 9! = 274,239`.
    - Our new goal is to find the 274,239th permutation of the remaining digits `[0, 1, 3, 4, 5, 6, 7, 8, 9]`.

5.  We repeat this process for the second digit, now with 8! permutations for the remaining 8 digits.
    - `274,239 / 8! = 274,239 / 40,320 = 6`.
    - The second digit is the digit at index 6 of the *remaining* digits, which is '7'.
    - Update the index: `274,239 % 8! = 32,319`.

6.  We continue this process until all digits have been chosen. This gives us the millionth permutation directly without generating any others.
"""
import math

def solve():
    """
    Finds the millionth lexicographic permutation of the digits 0-9.
    """
    digits = list(range(10))
    target_index = 1_000_000 - 1  # Using 0-based index
    
    result = []
    
    for i in range(10, 0, -1):
        # Calculate the factorial of the remaining digits
        f = math.factorial(i - 1)
        
        # Find the index of the digit to pick
        index = target_index // f
        
        # Get the digit and remove it from the list of available digits
        digit = digits.pop(index)
        result.append(str(digit))
        
        # Update the target index for the next iteration
        target_index %= f
        
    return "".join(result)

if __name__ == "__main__":
    print(solve())
