"""
Project Euler Problem 25: 1000-digit Fibonacci number

Problem:
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

Solution Idea:
We need to generate Fibonacci numbers and check the number of digits of each one until we find a term with 1000 digits. Since the numbers will become very large, we need a way to handle arbitrary-precision integers. Python's built-in integers are perfect for this.

1.  **Initialization:** We start with the first two Fibonacci numbers, F1 = 1 and F2 = 1. We can use two variables, `a` and `b`, to store the previous two terms in the sequence. Let `a = 1` and `b = 1`. We also need a counter for the index, starting at 2.

2.  **Iteration:** We will loop, calculating the next Fibonacci number by adding the previous two (`fib = a + b`).

3.  **Digit Check:** In each iteration, we check the number of digits in the newly calculated Fibonacci number. The easiest way to do this is to convert the number to a string and find its length: `len(str(fib))`.

4.  **Termination:** The loop continues until the length of the string representation of the Fibonacci number is 1000. When it is, we have found our target. The index counter at that point will be our answer.

5.  **Updating:** Inside the loop, after calculating the new term, we update our variables for the next iteration: `a` becomes `b`, and `b` becomes the new term. We also increment our index counter.
"""

def solve():
    """
    Finds the index of the first term in the Fibonacci sequence to contain 1000 digits.
    """
    # F1 and F2
    a, b = 1, 1
    index = 2
    
    # The number of digits in a number n is len(str(n))
    # We are looking for the first term with 1000 digits.
    
    while len(str(b)) < 1000:
        # Calculate the next term
        a, b = b, a + b
        index += 1
        
    return index

if __name__ == "__main__":
    print(solve())
