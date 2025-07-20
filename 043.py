"""
Project Euler Problem 43: Sub-string divisibility

Problem:
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:
- d2d3d4=406 is divisible by 2
- d3d4d5=063 is divisible by 3
- d4d5d6=635 is divisible by 5
- d5d6d7=357 is divisible by 7
- d6d7d8=572 is divisible by 11
- d7d8d9=728 is divisible by 13
- d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

Solution Idea:
The problem asks for the sum of all 0-to-9 pandigital numbers that satisfy a specific set of sub-string divisibility rules. A brute-force approach of generating all permutations and testing each one is feasible given that there are 10! (3,628,800) permutations, which is a manageable number for a modern computer.

1.  **Generate Permutations**: We will generate all permutations of the digits '0123456789'. The `itertools.permutations` function in Python is highly efficient for this.

2.  **Apply Constraints Sequentially**: For each generated permutation, we will check the divisibility rules one by one. We can apply the simplest constraints first to quickly discard non-qualifying numbers.
    - The number must be a 10-digit number, so the first digit cannot be '0'.
    - `d4d5d6` must be divisible by 5, which means `d6` must be '5'.
    - `d2d3d4` must be divisible by 2, which means `d4` must be an even digit.
    - And so on for the other divisibility rules (by 3, 7, 11, 13, 17).

3.  **Algorithm**:
    - Initialize a sum to 0.
    - Loop through each permutation of '0123456789'.
    - For each permutation, form the number string.
    - Check the conditions in an efficient order:
        1. Is `d1` zero? If so, skip.
        2. Check the divisibility of `d2d3d4` by 2.
        3. Check the divisibility of `d3d4d5` by 3.
        4. Check the divisibility of `d4d5d6` by 5.
        5. Check the divisibility of `d5d6d7` by 7.
        6. Check the divisibility of `d6d7d8` by 11.
        7. Check the divisibility of `d7d8d9` by 13.
        8. Check the divisibility of `d8d9d10` by 17.
    - If a number passes all the checks, convert it to an integer and add it to the total sum.

4.  **Final Result**: The final sum will be the answer.
"""
import itertools

def solve():
    """
    Finds the sum of all 0 to 9 pandigital numbers with the sub-string divisibility property.
    """
    total_sum = 0
    digits = '0123456789'
    
    for p in itertools.permutations(digits):
        # Skip numbers with a leading zero
        if p[0] == '0':
            continue
        
        # Check all divisibility properties
        if (int("".join(p[1:4])) % 2 == 0 and
            int("".join(p[2:5])) % 3 == 0 and
            int("".join(p[3:6])) % 5 == 0 and
            int("".join(p[4:7])) % 7 == 0 and
            int("".join(p[5:8])) % 11 == 0 and
            int("".join(p[6:9])) % 13 == 0 and
            int("".join(p[7:10])) % 17 == 0):
            
            total_sum += int("".join(p))
            
    return total_sum

if __name__ == "__main__":
    print(solve())
