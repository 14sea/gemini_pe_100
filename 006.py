"""
Solves the Project Euler Problem 6.

Question:
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385.
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025.
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Solution Idea:
The problem asks for the difference between two quantities for the first 100 natural numbers:
1. The sum of the squares: 1^2 + 2^2 + ... + 100^2
2. The square of the sum: (1 + 2 + ... + 100)^2

We can calculate these two quantities separately and then find their difference.

For the sum of the squares, we can loop from 1 to 100, square each number, and add it to a running total.

For the square of the sum, we can first find the sum of the numbers from 1 to 100, and then square the result.

There are also mathematical formulas for these sums:
- Sum of the first n natural numbers: n * (n + 1) / 2
- Sum of the squares of the first n natural numbers: n * (n + 1) * (2n + 1) / 6

Using these formulas would be more efficient than looping, but for n=100, a direct loop-based calculation is perfectly fine and easy to implement.

Let's stick to the direct calculation method as it's clear and sufficient for this problem size.
"""

def solve():
    n = 100
    
    # Calculate the sum of the squares
    sum_of_squares = sum(i*i for i in range(1, n + 1))
    
    # Calculate the square of the sum
    s = sum(range(1, n + 1))
    square_of_sum = s*s
    
    # Find the difference
    difference = square_of_sum - sum_of_squares
    
    print(difference)

solve()