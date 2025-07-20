"""
Project Euler Problem 57: Square root convergents

Problem:
It is possible to show that the square root of two can be expressed as an infinite continued fraction.
sqrt(2) = 1 + 1/(2 + 1/(2 + ...))

By expanding this for the first four iterations, we get:
1 + 1/2 = 3/2
1 + 1/(2 + 1/2) = 7/5
...
The eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

Solution Idea:
We need to generate the fractions for the first 1000 expansions and check the number of digits in the numerator and denominator for each. A direct calculation would be tedious, but we can find a recurrence relation.

Let the k-th expansion be F_k = N_k / D_k.
The structure is F_k = 1 + 1 / (1 + F_{k-1}), where we can consider the base case to be F_0 = 1.
Let's derive the recurrence. If F_{k-1} = n/d, then:
F_k = 1 + 1 / (1 + n/d) = 1 + 1 / ((d+n)/d) = 1 + d/(d+n) = (d+n+d)/(d+n) = (n + 2d) / (n+d).

This gives us the recurrence relations for the numerator and denominator:
N_k = N_{k-1} + 2 * D_{k-1}
D_k = N_{k-1} + D_{k-1}

We can start with the first expansion, N_1=3 and D_1=2, and then iterate 999 more times to get the first 1000 expansions. Python's arbitrary-precision integers are essential here, as the numbers will grow very large.

Algorithm:
1. Initialize numerator `num = 3` and denominator `den = 2`.
2. Initialize a counter `count = 0`.
3. Loop 999 times to generate the next 999 expansions (from the 2nd to the 1000th).
4. In each iteration, calculate the `next_num` and `next_den` using the recurrence relation.
5. Update `num` and `den`.
6. Check if the number of digits in the new numerator is greater than the number of digits in the new denominator. This can be done by comparing the lengths of their string representations.
7. If it is, increment the counter.
8. The final value of the counter is the answer.
"""

def solve():
    """
    Calculates how many of the first 1000 expansions of sqrt(2)
    have a numerator with more digits than the denominator.
    """
    # Start with the first expansion after the base 1/1
    num = 3
    den = 2
    count = 0
    
    # We already have the first expansion, so we loop 999 times for the rest.
    for _ in range(999):
        # Calculate the next term using the recurrence relation
        # N_k = N_{k-1} + 2*D_{k-1}
        # D_k = N_{k-1} + D_{k-1}
        next_num = num + 2 * den
        next_den = num + den
        
        num = next_num
        den = next_den
        
        # Check if the numerator has more digits than the denominator
        if len(str(num)) > len(str(den)):
            count += 1
            
    return count

if __name__ == "__main__":
    print(solve())
