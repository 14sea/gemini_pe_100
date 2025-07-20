"""
Solves the Project Euler Problem 1.

Question:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Solution Idea:
We can iterate through all the numbers from 1 to 999.
For each number, we check if it is divisible by 3 or 5.
If it is, we add it to a running total.
Finally, we print the total sum.
"""

def solve():
    total_sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    print(total_sum)

solve()