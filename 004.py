"""
Solves the Project Euler Problem 4.

Question:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Solution Idea:
We are looking for the largest palindrome that is a product of two 3-digit numbers.
Since we want the largest palindrome, we should start our search from the largest possible products.

The largest 3-digit number is 999. So, we can use nested loops to check the product of all pairs of 3-digit numbers.
We can iterate downwards from 999 to 100 for both numbers.

For each product, we need to check two things:
1. Is it a palindrome?
2. Is it larger than the largest palindrome found so far?

To check if a number is a palindrome, we can convert it to a string and see if the string is equal to its reverse.

We can optimize the search slightly. If we have loops for `i` and `j` both from 999 down to 100, we can make the inner loop for `j` go from `i` down to 100. This avoids checking the same pair of numbers twice (e.g., 999*998 and 998*999).

We can also add a break condition. If the product `i * j` becomes smaller than the `largest_palindrome` we've already found, we know that no further products in the inner loop (for the current `i`) can be larger, so we can break out of it and move to the next `i`.
"""

def solve():
    largest_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product <= largest_palindrome:
                break
            if str(product) == str(product)[::-1]:
                largest_palindrome = product
    print(largest_palindrome)

solve()