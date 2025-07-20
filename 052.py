"""
Project Euler Problem 52: Permuted multiples

Problem:
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

Solution Idea:
We are looking for the smallest positive integer `x` that satisfies the condition. This suggests a straightforward search, starting from `x=1` and incrementing until we find our answer.

1.  **Search Strategy**: We will iterate through integers `x` starting from 1. The first number that satisfies the conditions will be the smallest, and thus our answer.

2.  **Permutation Check**: The core of the problem is to check if two numbers "contain the same digits". An easy and reliable way to do this is to convert both numbers to strings, sort the characters of the strings, and check if the sorted versions are identical. For example, `sorted("125874")` is the same as `sorted("251748")`.

3.  **Algorithm**:
    a.  Start a loop with `x = 1`.
    b.  For each `x`, first get the "canonical" representation of its digits by creating a sorted list of its digit characters: `digits_x = sorted(str(x))`.
    c.  Then, check each of the multiples `2x, 3x, 4x, 5x, 6x`.
    d.  For each multiple `m`, calculate its sorted digits: `digits_m = sorted(str(m))`.
    e.  Compare `digits_m` with `digits_x`. If they are not the same at any point, then this `x` is not the solution. We break the check for the current `x` and move to `x + 1`.
    f.  If `x` passes the check for all multiples from 2x to 6x, we have found our answer. We can then terminate the search and return `x`.

4.  **Optimization**: For `6x` to have the same number of digits as `x`, `x` must start with the digit '1'. For example, if `x` is 200, `6x` is 1200, which has more digits. This means we don't need to check every integer, but a simple incremental search is fast enough to find the solution quickly.
"""

def solve():
    """
    Finds the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
    """
    x = 1
    while True:
        digits_x = sorted(str(x))
        
        # Check multiples from 2x to 6x
        is_solution = True
        for i in range(2, 7):
            multiple = x * i
            if sorted(str(multiple)) != digits_x:
                is_solution = False
                break
        
        if is_solution:
            return x
            
        x += 1

if __name__ == "__main__":
    print(solve())
