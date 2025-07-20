"""
Project Euler Problem 93: Arithmetic expressions

Problem:
Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained by using each of the digits exactly once, the four arithmetic operations (+, -, *, /), and parentheses.

Solution Idea:
The problem requires a systematic search through all possible combinations of digits and operations.

1.  **Iterate Digit Sets**: We first generate all combinations of 4 distinct digits from {0, 1, ..., 9}. There are C(10, 4) = 210 such sets.

2.  **Generate Expressions**: For each set of 4 digits, we need to find all possible integer values that can be formed. This involves considering:
    - All permutations of the 4 digits (4! = 24 ways).
    - All combinations of 3 operators from {+, -, *, /} (4^3 = 64 ways).
    - All valid ways to apply parentheses. For 4 numbers, there are 5 distinct structures, but by permuting the numbers, we only need to check two main patterns: `((a op b) op c) op d` and `(a op b) op (c op d)`.

3.  **Evaluate and Collect**: We can use Python's `eval()` function to safely evaluate the string expressions we generate. We must handle `ZeroDivisionError`. All positive integer results are collected into a set to store the unique targets.

4.  **Check Consecutive Sequence**: For each set of digits, after finding all its targets, we check for the longest sequence of consecutive integers starting from 1. We find the smallest positive integer `n` that is *not* in our set of targets. The length of the sequence is `n-1`.

5.  **Find Maximum**: We keep track of the digit set that produces the longest sequence and return it as the answer.
"""
import itertools

def solve():
    """
    Finds the set of four distinct digits, a < b < c < d, for which the
    longest set of consecutive positive integers, 1 to n, can be obtained.
    """
    max_n = 0
    best_digits_tuple = None
    ops = ['+', '-', '*', '/']

    # Iterate through all combinations of 4 distinct digits
    for digits in itertools.combinations(range(10), 4):
        targets = set()
        # Iterate through all permutations of these 4 digits
        for p in itertools.permutations(digits):
            a, b, c, d = map(str, p)
            # Iterate through all combinations of 3 operators
            for op1, op2, op3 in itertools.product(ops, repeat=3):
                # We only need to check two parenthesis structures, as the digit
                # permutations cover the other structural variations.
                
                # Pattern 1: ((a op b) op c) op d
                expr1 = f"(({a} {op1} {b}) {op2} {c}) {op3} {d}"
                try:
                    targets.add(eval(expr1))
                except (ZeroDivisionError, SyntaxError):
                    pass

                # Pattern 2: (a op b) op (c op d)
                expr2 = f"({a} {op1} {b}) {op2} ({c} {op3} {d})"
                try:
                    targets.add(eval(expr2))
                except (ZeroDivisionError, SyntaxError):
                    pass
        
        # Filter for positive integers
        positive_integers = {int(x) for x in targets if x is not None and x > 0 and x == int(x)}
        
        # Find the length of the consecutive sequence from 1
        n = 0
        while n + 1 in positive_integers:
            n += 1
            
        if n > max_n:
            max_n = n
            best_digits_tuple = digits
            
    return "".join(map(str, best_digits_tuple))

if __name__ == "__main__":
    print(solve())
