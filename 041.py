"""
Project Euler Problem 41: Pandigital prime

Problem:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

Solution Idea:
We are looking for the largest prime number that is also pandigital. This suggests we should start our search from the largest possible pandigital numbers and work our way down.

1.  **Determine the maximum `n`**:
    The largest possible value for `n` is 9 (a 9-digit number using digits 1-9).

2.  **Use the Divisibility Rule of 3**:
    A key optimization is to check the sum of the digits for each `n`. If the sum of the digits is divisible by 3, then any number formed by those digits will also be divisible by 3, and therefore cannot be prime (unless it is 3 itself, which is not the case here).
    - Sum of digits 1-9: `1+2+...+9 = 45` (divisible by 3). So, no 9-digit pandigital prime exists.
    - Sum of digits 1-8: `1+2+...+8 = 36` (divisible by 3). No 8-digit pandigital prime exists.
    - Sum of digits 1-7: `1+2+...+7 = 28` (not divisible by 3). 7-digit pandigital primes *might* exist.
    - Sum of digits 1-6: `1+2+...+6 = 21` (divisible by 3). No 6-digit pandigital prime.
    - Sum of digits 1-5: `1+2+...+5 = 15` (divisible by 3). No 5-digit pandigital prime.
    - Sum of digits 1-4: `1+2+...+4 = 10` (not divisible by 3). 4-digit pandigital primes *might* exist.

    This tells us the largest possible pandigital prime must be either 7-digit or 4-digit. Since any 7-digit number is larger than any 4-digit number, we only need to search for the largest 7-digit pandigital prime.

3.  **Algorithm**:
    - We will generate all permutations of the digits `1, 2, 3, 4, 5, 6, 7`.
    - To find the largest prime, we should check the permutations in descending order. We can do this by generating permutations of the digits sorted in descending order: `(7, 6, 5, 4, 3, 2, 1)`.
    - For each permutation, we form the number and check if it's prime.
    - The very first prime number we find will be the largest one, and we can stop our search.

4.  **Primality Test**:
    - We need a standard `is_prime` function. For numbers up to 7 digits, a trial division check up to the square root of the number is efficient enough.
"""
import math
import itertools

def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def solve():
    """
    Finds the largest n-digit pandigital prime that exists.
    """
    # From the divisibility rule, we only need to check n=7 and n=4.
    # We start with n=7 to find the largest possible prime.
    
    # Check for 7-digit pandigital primes
    digits_7 = '7654321'
    for p in itertools.permutations(digits_7):
        num = int("".join(p))
        if is_prime(num):
            return num # This is the largest, so we can stop.
            
    # If no 7-digit found, check for 4-digit pandigital primes
    digits_4 = '4321'
    for p in itertools.permutations(digits_4):
        num = int("".join(p))
        if is_prime(num):
            return num # This would be the largest if no 7-digit one exists.
            
    return None # Should not be reached based on the problem's premise

if __name__ == "__main__":
    print(solve())
