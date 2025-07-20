"""
Project Euler Problem 23: Non-abundant sums

Problem:
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Solution Idea:
1.  **Find all abundant numbers:** We need to find all abundant numbers up to the limit of 28123. An abundant number is a number where the sum of its proper divisors is greater than the number itself. We can create a helper function `sum_proper_divisors(n)` to calculate this sum.
2.  **Generate sums of two abundant numbers:** Create a list of all abundant numbers found in step 1. Then, generate all possible sums of two numbers from this list. We only need to consider sums that are less than or equal to 28123. A boolean array (or a set) is a good way to keep track of which numbers can be formed by the sum of two abundant numbers.
3.  **Identify non-abundant sums:** The numbers that *cannot* be expressed as the sum of two abundant numbers are the ones not marked in our boolean array from step 2.
4.  **Calculate the final sum:** Sum up all the numbers from 1 to 28123 that were not marked in the boolean array. This sum is our final answer.
"""

def sum_proper_divisors(n):
    """
    Calculates the sum of proper divisors of a number n.
    """
    if n < 2:
        return 0
    
    s = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s += i
            if i * i != n:
                s += n // i
    return s

def solve():
    """
    Finds the sum of all positive integers which cannot be written as the sum of two abundant numbers.
    """
    limit = 28123
    
    # 1. Find all abundant numbers
    abundant_numbers = []
    for i in range(12, limit + 1):
        if sum_proper_divisors(i) > i:
            abundant_numbers.append(i)
            
    # 2. Generate sums of two abundant numbers
    can_be_written_as_sum = [False] * (limit + 1)
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            s = abundant_numbers[i] + abundant_numbers[j]
            if s <= limit:
                can_be_written_as_sum[s] = True
            else:
                # Since the list is sorted, no further sums with this i will be within the limit
                break

    # 3. & 4. Find and sum the numbers that cannot be written as a sum of two abundant numbers
    total_sum = 0
    for i in range(1, limit + 1):
        if not can_be_written_as_sum[i]:
            total_sum += i
            
    return total_sum

if __name__ == "__main__":
    print(solve())
