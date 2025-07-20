"""
Project Euler Problem 30: Digit fifth powers

Problem:
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

Solution Idea:
First, we need to determine an upper bound for the numbers to check. We can't check numbers indefinitely.

Let's consider a number with `d` digits.
The smallest `d`-digit number is `10^(d-1)`.
The largest possible sum of the fifth powers of the digits for a `d`-digit number is `d * 9^5`.
Let's calculate `9^5 = 59049`.

- For d=1, max sum = 1 * 59049 = 59049.
- For d=2, max sum = 2 * 59049 = 118098.
- For d=3, max sum = 3 * 59049 = 177147.
- For d=4, max sum = 4 * 59049 = 236196.
- For d=5, max sum = 5 * 59049 = 295245.
- For d=6, max sum = 6 * 59049 = 354294.
- For d=7, max sum = 7 * 59049 = 413343. The smallest 7-digit number is 1,000,000.

Since the maximum possible sum for a 7-digit number (413,343) is less than the smallest 7-digit number (1,000,000), no 7-digit number (or any number with more digits) can be equal to the sum of the fifth powers of its digits.
Therefore, we only need to check numbers up to the maximum possible sum for a 6-digit number, which is 354,294.

The algorithm is as follows:
1. Iterate through numbers from 2 up to our calculated limit (354,294). We start at 2 because 1 is not considered a sum.
2. For each number, calculate the sum of the fifth powers of its digits.
3. If the sum is equal to the number itself, add it to a list of results.
4. Finally, sum all the numbers in our results list.
"""

def solve():
    """
    Finds the sum of all numbers that can be written as the sum of the fifth powers of their digits.
    """
    # Upper limit is 6 * (9^5) = 354294
    limit = 354294
    found_numbers = []
    
    # Start from 10, as single-digit numbers are not sums.
    for n in range(10, limit + 1):
        sum_of_powers = 0
        for digit in str(n):
            sum_of_powers += int(digit)**5
        
        if sum_of_powers == n:
            found_numbers.append(n)
            
    return sum(found_numbers)

if __name__ == "__main__":
    print(solve())
