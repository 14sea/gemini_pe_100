"""
Project Euler Problem 56: Powerful digit sum

Problem:
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

Solution Idea:
We need to check all possible combinations of a and b within the given range and find the one that produces the largest sum of digits.

1.  **Brute-Force Search**: Since the ranges for `a` and `b` are small (1 to 99), a simple brute-force approach is perfectly feasible. We will iterate through all possible pairs.

2.  **Handling Large Numbers**: The numbers `a^b` can become very large (e.g., 99^99). Python's built-in support for arbitrary-precision integers handles this automatically, so we don't need to worry about overflow.

3.  **Calculating Digital Sum**: For each calculated number `a^b`, we need to find the sum of its digits. The most straightforward way to do this is:
    a. Convert the large integer to a string.
    b. Iterate through each character in the string.
    c. Convert each character back to an integer and add it to a running total.

4.  **Algorithm**:
    a. Initialize a variable `max_digital_sum` to 0.
    b. Create a nested loop: the outer loop for `a` from 1 to 99, and the inner loop for `b` from 1 to 99.
    c. Inside the loops, calculate `power = a**b`.
    d. Calculate the `current_digital_sum` of `power`.
    e. Compare `current_digital_sum` with `max_digital_sum`. If it's larger, update `max_digital_sum`.
    f. After the loops complete, `max_digital_sum` will hold the final answer.
"""

def solve():
    """
    Finds the maximum digital sum for numbers of the form a^b, where a, b < 100.
    """
    max_digital_sum = 0
    
    # a and b are less than 100, so they go from 1 to 99.
    for a in range(1, 100):
        for b in range(1, 100):
            power = a**b
            
            # Calculate the digital sum
            current_digital_sum = sum(int(digit) for digit in str(power))
            
            if current_digital_sum > max_digital_sum:
                max_digital_sum = current_digital_sum
                
    return max_digital_sum

if __name__ == "__main__":
    print(solve())
