"""
Project Euler Problem 26: Reciprocal cycles

Problem:
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

Solution Idea:
The length of the recurring cycle in the decimal representation of 1/d can be found by simulating the long division process.

1.  We perform division of 1 by d. In each step of the long division, we get a remainder. We then multiply this remainder by 10 to get the next numerator for the division.
2.  The sequence of digits in the decimal part starts repeating as soon as we encounter a remainder that has been seen before.
3.  The length of the cycle is the number of steps between the first and second occurrences of any remainder.
4.  We can write a function `get_cycle_length(d)` that takes a denominator `d` and calculates the length of its recurring cycle.
    - Inside this function, we'll use a dictionary to store the remainders we've encountered and the position (step number) at which they appeared.
    - We start with a remainder of 1.
    - In a loop, we calculate `remainder = (remainder * 10) % d`.
    - If the `remainder` becomes 0, the decimal terminates, and the cycle length is 0.
    - If we see a `remainder` that is already in our dictionary of remainders, we have found a cycle. The length of this cycle is the current position minus the position stored for that remainder.
5.  We then iterate through all `d` from 2 to 999, call our function for each `d`, and keep track of the `d` that gives the longest cycle length.
"""

def get_cycle_length(d):
    """
    Calculates the length of the recurring cycle of 1/d.
    """
    remainders = {}
    remainder = 1
    position = 0
    
    while remainder != 0 and remainder not in remainders:
        remainders[remainder] = position
        remainder = (remainder * 10) % d
        position += 1
        
    if remainder == 0:
        return 0
    else:
        # The cycle length is the current position minus the position where the remainder was first seen.
        return position - remainders[remainder]

def solve():
    """
    Finds the value of d < 1000 for which 1/d has the longest recurring cycle.
    """
    max_length = 0
    result_d = 0
    
    for d in range(2, 1000):
        length = get_cycle_length(d)
        if length > max_length:
            max_length = length
            result_d = d
            
    return result_d

if __name__ == "__main__":
    print(solve())
