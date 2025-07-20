import math

def solve():
    """
    Solves the Project Euler Problem 20.

    Question:
    n! means n × (n - 1) × ... × 3 × 2 × 1.
    For example, 10! = 3628800, and the sum of the digits in the number 10!
    is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!.

    Solution Idea:
    The solution involves two main steps. First, we calculate the value of 100!.
    Python's `math.factorial()` function is perfect for this, and its standard
    integer type can handle the resulting large number without any overflow issues.

    Second, once we have the number, we need to sum its digits. The most
    direct way to do this is to convert the large integer into a string.
    This allows us to iterate over each character (digit), convert it back
    to an integer, and add it to a total sum.
    """
    number = math.factorial(100)
    
    sum_of_digits = sum(int(digit) for digit in str(number))
    
    print(f"The sum of the digits in 100! is: {sum_of_digits}")

solve()