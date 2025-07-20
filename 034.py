"""
Project Euler Problem 34: Digit factorials

Problem:
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

Solution Idea:
First, we need to establish an upper bound for the numbers to check. We can't check numbers indefinitely.

Let's pre-calculate the factorials of the digits 0-9:
0! = 1, 1! = 1, 2! = 2, 3! = 6, 4! = 24, 5! = 120, 6! = 720, 7! = 5040, 8! = 40320, 9! = 362880.

The largest possible sum of digit factorials for a number with `d` digits is `d * 9!`.
- For a 7-digit number, the maximum sum is 7 * 362880 = 2,540,160.
- For an 8-digit number, the maximum sum is 8 * 362880 = 2,903,040, which is only a 7-digit number.
This means that no number with 8 or more digits can be equal to the sum of the factorials of its digits, because the sum will always have fewer digits than the number itself.
So, our search is bounded. A safe upper limit is 2,540,160.

The algorithm is as follows:
1.  Pre-compute and cache the factorials of digits 0-9.
2.  Iterate through numbers from 10 up to our limit (2,540,160). We start at 10 because 1 and 2 are excluded as they are not sums.
3.  For each number, calculate the sum of the factorials of its digits.
4.  If the sum is equal to the number itself, it's a "curious number".
5.  Add all such numbers to find the final sum.
"""
import math

def solve():
    """
    Finds the sum of all numbers which are equal to the sum of the factorial of their digits.
    """
    # Pre-calculate factorials for digits 0-9
    factorials = [math.factorial(i) for i in range(10)]
    
    curious_numbers = []
    
    # Upper bound is 7 * 9! = 2,540,160
    limit = 2540160
    
    # Start from 10 as 1! and 2! are not sums.
    for n in range(10, limit + 1):
        sum_of_factorials = 0
        temp_n = n
        while temp_n > 0:
            digit = temp_n % 10
            sum_of_factorials += factorials[digit]
            temp_n //= 10
            
        if sum_of_factorials == n:
            curious_numbers.append(n)
            
    return sum(curious_numbers)

if __name__ == "__main__":
    print(solve())
