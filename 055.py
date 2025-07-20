"""
Project Euler Problem 55: Lychrel numbers

Problem:
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
Not all numbers produce palindromes so quickly. For example, 349 took three iterations.

A number that never forms a palindrome through the reverse and add process is called a Lychrel number. For the purpose of this problem, we shall assume that a number is Lychrel if it does not become a palindrome within fifty iterations.

How many Lychrel numbers are there below ten-thousand?

Solution Idea:
We need to check every number from 1 to 9999 to see if it's a Lychrel number according to the problem's definition.

1.  **Palindrome Check**: We need a helper function to check if a number is a palindrome. The easiest way is to convert the number to a string and check if the string is equal to its reverse.

2.  **Lychrel Check Function**: We will create a function, say `is_lychrel(n)`, that takes a number `n` and determines if it's a Lychrel number.
    - This function will perform the "reverse and add" process for a maximum of 50 iterations.
    - It starts with the given number `n`.
    - In a loop that runs up to 50 times:
        a. It reverses the current number.
        b. It adds the reversed number to the current number.
        c. It checks if the new sum is a palindrome.
        d. If it is a palindrome, the number is *not* a Lychrel number, and the function can return `False`.
    - If the loop completes all 50 iterations without producing a palindrome, we assume the number is a Lychrel number and the function returns `True`.

3.  **Main Loop**:
    - We initialize a counter for Lychrel numbers to 0.
    - We loop through all numbers `i` from 1 to 9999.
    - For each `i`, we call our `is_lychrel(i)` function.
    - If the function returns `True`, we increment our counter.

4.  **Final Result**: The final value of the counter will be the answer.
"""

def is_palindrome(n):
    """Checks if a number is a palindrome."""
    return str(n) == str(n)[::-1]

def is_lychrel(n):
    """
    Checks if a number is a Lychrel number (does not form a palindrome within 50 iterations).
    """
    current_num = n
    for _ in range(50):
        reversed_num = int(str(current_num)[::-1])
        current_num += reversed_num
        if is_palindrome(current_num):
            return False # It's not a Lychrel number
    
    # If we reach here after 50 iterations, it's considered a Lychrel number for this problem.
    return True

def solve():
    """
    Counts the number of Lychrel numbers below ten-thousand.
    """
    lychrel_count = 0
    for i in range(1, 10000):
        if is_lychrel(i):
            lychrel_count += 1
            
    return lychrel_count

if __name__ == "__main__":
    print(solve())
