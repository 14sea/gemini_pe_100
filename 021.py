"""
Project Euler Problem 21: Amicable numbers

Problem:
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Solution Idea:
To find the amicable numbers, we need to calculate the sum of proper divisors for each number up to the limit (10000).
Let's define a function `sum_proper_divisors(n)` that calculates d(n). To do this efficiently, we can iterate from 2 up to the square root of n. If a number `i` divides `n`, then both `i` and `n/i` are divisors. We add both to our sum. We initialize the sum with 1 to account for the divisor 1.

Once we have this function, we can iterate through all numbers `a` from 2 to 10000. For each `a`, we calculate `b = d(a)`. Then we check if `d(b) == a`.
There's a condition that `a` and `b` must not be equal (`a ≠ b`).
If these conditions are met, `a` is an amicable number, and we add it to our total sum.

To make this more efficient, we can pre-calculate and store the sum of proper divisors for all numbers up to 10000 in an array or list. This avoids re-calculating `d(n)` multiple times.
"""

def sum_proper_divisors(n):
    """
    Calculates the sum of proper divisors of a number n.
    """
    if n < 2:
        return 0
    
    s = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s += i
            if i * i != n:
                s += n // i
    return s

def solve():
    """
    Finds the sum of all amicable numbers under 10000.
    """
    limit = 10000
    d_values = [0] * limit
    for i in range(1, limit):
        d_values[i] = sum_proper_divisors(i)
    
    amicable_sum = 0
    for a in range(2, limit):
        b = d_values[a]
        if b < limit and a != b:
            if d_values[b] == a:
                amicable_sum += a
    
    return amicable_sum

if __name__ == "__main__":
    print(solve())
